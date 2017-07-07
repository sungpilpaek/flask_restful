""" Main module for running the webpage using app.run
"""
from apis import clicors_api
from flask_restful import Api
from database import initialization_db, clicors_db
from flask import Flask, render_template, g, Response
from common import exception, config, message, log, sse

""" WSGI assumes the instance of Flask will be named, 'application'.
    Due to my laziness, tweaked below so that application refers to app.
"""
application = Flask(__name__)

app = application
app.config["DEBUG"] = config.DEBUG
app.config["LOGGER_NAME"] = config.LOGGER_NAME
app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = \
    config.PRESERVE_CONTEXT_ON_EXCEPTION
app.config["THREADED"] = True

""" Register ERROR messages when declaring api.
"""
api = Api(app, errors=exception.ERRORS)


@app.route("/")
def index():
    """ A view function for root endpoint. Returns html for visual aids.
    """
    return render_template("index.html"), message.STATUS_OK


@app.route('/stream/')
def stream():
    """ Implementation of Server Sent Event
    """
    return Response(
        sse.event_stream(app),
        mimetype="text/event-stream"
    )


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
    clicors_api.Manager,
    "/api/v1/clicors",
    resource_class_kwargs={
        "ClicorsDbManager": clicors_db.Manager
    },
    endpoint="clicors"
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


""" Run app.py here.
"""
if __name__ == "__main__":
    app.run("", threaded=True)