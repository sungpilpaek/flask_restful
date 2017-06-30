""" Main module for running the webpage using app.run
"""
from flask_restful import Api
from resources import subscribers_api
from database import initializer, subscriber
from common import exception, config, message, log
from flask import Flask, render_template, request, abort, url_for, jsonify


app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG
app.config['LOGGER_NAME'] = config.LOGGER_NAME

""" Register ERROR messages at errors keyword argument.
"""
api = Api(app, errors=exception.ERRORS)


@app.route('/')
def index():
    return render_template('index.html'), message.STATUS_OK


def initializeDatabase():
    database_object = initializer.Initializer()
    database_object.initialize_db_creating_schema()


if __name__ == '__main__':
    initializeDatabase()

    """ Register APIs here.
    """
    api.add_resource(
        subscribers_api.Subscribers,
        '/api/v1/subscribers',
        resource_class_kwargs={
            'subscriber': subscriber.Subscriber
        },
        endpoint="subscribers"
    )

    """ Register Logger here.
    """
    if not app.debug:
        handler = log.getLogHandler()
        app.logger.addHandler(handler)
        app.logger.setLevel(config.LOGGING_LEVEL)

    """ Run app.py here.
    """
    app.run('0.0.0.0', int("5000"), threaded=True)