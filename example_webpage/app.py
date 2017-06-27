""" A Example Webpage For Subscriptions

"""
from flask import Flask, render_template, request, abort
from flask_restful import Api, reqparse
from database.sqlite import *


def parse_arg_from_requests(arg, **kwargs):
    parse = reqparse.RequestParser()
    parse.add_argument(arg, **kwargs)
    args = parse.parse_args()
    return args[arg]


initialize_db_creating_schema()
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transaction', methods=['POST'])
def transaction():
    if request.method == 'POST':
        username = request.json['username']
        user = Subscriber(username)
        if user.db_insert() == "INSERT_FAIL_NULL_VALUE":
            abort(400)

        return username


# @app.teardown_appcontext
# def tmp():
#     print "BYEBYE!"


if __name__ == '__main__':
    app.run('0.0.0.0', int("5000"), threaded=True)