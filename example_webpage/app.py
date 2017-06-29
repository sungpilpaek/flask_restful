""" Main module for running the webpage using app.run
"""
from database import sqlite
from flask_restful import Api
from resources import subscribers_api
from common import exception, config, message
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, abort, url_for, jsonify
import logging


app = Flask(__name__)
""" Register ERROR messages at errors keyword argument.
"""
api = Api(app, errors=exception.ERRORS)


@app.route('/')
def index():
    return render_template('index.html'), message.STATUS_OK


if __name__ == '__main__':
    sqlite.initialize_db_creating_schema()

    """ Register APIs here.
    """
    api.add_resource(
        subscribers_api.GetSubscribers,
        '/api/v1/get/subscribers',
        resource_class_kwargs={'query_all': sqlite.query_subscribers},
        endpoint="getsubscribers"
    )

    api.add_resource(
        subscribers_api.PostSubscribers,
        '/api/v1/post/subscribers',
        resource_class_kwargs={'subscriber': sqlite.Subscriber},
        endpoint="postsubscribers"
    )

    """ Register Logger here.
    """
    if not app.debug:
        file_handler = RotatingFileHandler(
            config.LOG_PATH,
            maxBytes=config.LOG_MAX_BYTE,
            backupCount=config.LOG_BACKUP_COUNT
        )
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

    """ Run app.py
    """
    app.run('0.0.0.0', int("5000"), threaded=True)