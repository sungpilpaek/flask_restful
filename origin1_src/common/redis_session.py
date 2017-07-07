""" Custom session interface which uses Redis as a backend session storage.
"""
from uuid import uuid4
from redis import StrictRedis
from datetime import timedelta
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin
import pickle
import config


class RedisSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, session_id=None, is_new=False):
        self.session_id = session_id
        self.is_new = is_new
        self.modified = False

        """ CallbackDict calls on_update function whenever there's a change
            in a session (e.g. update/insert in k/v)
        """
        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial, on_update)


class RedisSessionInterface(SessionInterface):
    def __init__(self, prefix="session:"):
        self.redis = StrictRedis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=config.REDIS_DB
        )

        self.prefix = prefix

    def _generate_session_id(self):
        return str(uuid4())

    def open_session(self, app, request):
        """ Flask requires implementaion of open_session() and save_session()
            when creating custom session interface.
        """
        session_id = request.cookies.get(app.session_cookie_name)
        if not session_id:
            session_id = self._generate_session_id()

            return RedisSession(session_id=session_id, is_new=True)

        serialized_data = self.redis.get(self.prefix + session_id)
        if serialized_data is not None:
            data = pickle.loads(serialized_data)

            return RedisSession(data, session_id=session_id)

        return RedisSession(session_id=session_id, is_new=True)

    def _get_expiration_time_redis(self, app, session):
        if session.permanent:
            return app.permanent_session_lifetime

        return timedelta(days=1)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)

        """ When session does not contain any meaningful information.
            (i.e. dict(session) -> {})
        """
        if not session:
            self.redis.delete(self.prefix + session.session_id)
            if session.modified:
                response.delete_cookie(
                    app.session_cookie_name,
                    domain=domain
                )

            return

        expiration_time_redis = self._get_expiration_time_redis(app, session)
        expiration_time_cookie = self.get_expiration_time(app, session)
        serialized_data = pickle.dumps(dict(session))

        self.redis.setex(
            self.prefix + session.session_id,
            int(expiration_time_redis.total_seconds()),
            serialized_data
        )

        response.set_cookie(
            app.session_cookie_name,
            session.session_id,
            expires=expiration_time_cookie,
            httponly=True,
            domain=domain
        )