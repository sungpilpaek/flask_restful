""" A Example Webpage For Subscriptions

"""
from flask import Flask, render_template, request, abort
from flask_restful import Api
from database.sqlite import *
from resources.subscribers_api import *


app = Flask(__name__)
api = Api(app)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transaction', methods=['POST'])
def transaction():
    if request.method == 'POST':
        username = request.json['username']
        user = Subscriber(username)
        if user.insert_to_db() == "INSERT_FAIL_NULL_VALUE":
            abort(400)

        return username


if __name__ == '__main__':
    initialize_db_creating_schema()

    api.add_resource(
        SubscribersAPI,
        '/api/v1/subscribers',
        resource_class_kwargs={'query_all': query_all_subscribers}
    )

    app.run('0.0.0.0', int("5000"), threaded=True)