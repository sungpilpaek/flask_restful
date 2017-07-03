""" Main module for running the webpage using app.run
"""
from flask_restful import Api
from apis import api_subscription
from common import exception, config, message, log
from database import db_initialization, db_subscription
from flask import Flask, render_template, request, abort, url_for, jsonify


app = Flask(__name__)
app.config["DEBUG"] = config.DEBUG
app.config["LOGGER_NAME"] = config.LOGGER_NAME

""" Register ERROR messages when declaring api.
"""
api = Api(app, errors=exception.ERRORS)


@app.route("/")
def index():
    """ A view function for root endpoint. Returns html for visual aids.
    """
    return render_template("index.html"), message.STATUS_OK


def initializeDatabase():
    manager = db_initialization.Manager()
    manager.create_schema()


if __name__ == "__main__":
    """ Create database when you run this app for first time, or the .db
        file was removed.
    """
    initializeDatabase()

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
        api_subscription.Manager,
        "/api/v1/subscription",
        resource_class_kwargs={
            "DbSubscriptionManager": db_subscription.Manager
        },
        endpoint="subscription"
    )

    """ Register Logger here.
    """
    if not app.debug:
        handler = log.getLogHandler()
        app.logger.addHandler(handler)
        app.logger.setLevel(config.LOGGING_LEVEL)

    """ Run app.py here.
    """
    app.run("0.0.0.0", int("5000"), threaded=True)