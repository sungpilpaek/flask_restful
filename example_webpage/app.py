""" Main module for running the webpage using app.run
    
"""
from database import sqlite
from flask_restful import Api
from resources import subscribers_api
from common import util, exception_handler
from flask import Flask, render_template, request, abort, url_for, jsonify


app = Flask(__name__)
api = Api(app)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html'), util.STATUS_OK


@app.errorhandler(exception_handler.ExtendedAbort)
def handle_invalid_usage(error):
    """ Errorhandler for user's invalid parameter.
    
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


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

    app.run('0.0.0.0', int("5000"), threaded=True)