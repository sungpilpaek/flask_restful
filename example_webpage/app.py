""" A Example Webpage For Subscriptions

"""
from common import util
from database import sqlite
from flask_restful import Api
from resources import subscribers_api
from flask import Flask, render_template, request, abort, url_for


app = Flask(__name__)
api = Api(app)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html'), util.STATUS_OK


if __name__ == '__main__':
    sqlite.initialize_db_creating_schema()

    api.add_resource(
        subscribers_api.GetSubscribers,
        '/api/v1/get/subscribers',
        resource_class_kwargs={'query_all': sqlite.query_all_subscribers},
        endpoint="getsubscribers"
    )

    api.add_resource(
        subscribers_api.PostSubscribers,
        '/api/v1/post/subscribers',
        resource_class_kwargs={'subscriber': sqlite.Subscriber},
        endpoint="postsubscribers"
    )

    app.run('0.0.0.0', int("5000"), threaded=True)