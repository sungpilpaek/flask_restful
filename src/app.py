""" Main module for running the webpage using app.run
"""
from flask_restful import Api
from apis import subscription_api
from flask import Flask, render_template, g, session
from database import initialization_db, subscription_db
from common import exception, config, message, log, redis_session

""" WSGI assumes the instance of Flask will be named, 'application'.
    Due to my laziness, tweaked below so that application refers to app.
"""
application = Flask(__name__)

app = application
app.config["DEBUG"] = config.DEBUG
app.config["LOGGER_NAME"] = config.LOGGER_NAME
app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = \
    config.PRESERVE_CONTEXT_ON_EXCEPTION

""" Register ERROR messages when declaring api.
"""
api = Api(app, errors=exception.ERRORS)


@app.route("/")
def index():
    """ A view function for root endpoint. Returns html for visual aids.
    """
    return render_template("index.html"), message.STATUS_OK


@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()


def initializeDatabase():
    with app.app_context():
        manager = initialization_db.Manager()
        manager.create_schema()


""" Register APIs here.

Parameters:
    add_resource(
        API_CLASS,                  : Your api class.
        URL1,                       : Multiple urls.
        URL2,                       : Multiple urls.
        RESOURCE_CLASS_KWARGS={     : Other util "objects" which you want to
            NAME1: USER_CLASS1,       use inside api class.
            NAME2: USER_CLASS2
        },
        ENDPOINT="something"        : Useful when using url_for() in
    )                                 jinja2 template.
"""

api.add_resource(
    subscription_api.Manager,
    "/api/v1/subscription",
    resource_class_kwargs={
        "SubscriptionDbManager": subscription_db.Manager
    },
    endpoint="subscription"
)

""" Create database when you run this app for first time, or the .db
    file was removed.
"""
initializeDatabase()

""" Register Logger here.
"""
if not app.debug:
    handler = log.getLogHandler()
    app.logger.addHandler(handler)
    app.logger.setLevel(config.LOGGING_LEVEL)

""" Register session interface here.
"""
app.session_interface = redis_session.RedisSessionInterface()

""" Run app.py here.
"""

if __name__ == "__main__":
    app.run("0.0.0.0", threaded=True)