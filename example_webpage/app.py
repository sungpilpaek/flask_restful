""" A Example Webpage For Subscriptions

"""
from flask import Flask, render_template, request
from flask_restful import Api, reqparse


def parse_arg_from_requests(arg, **kwargs):
    parse = reqparse.RequestParser()
    parse.add_argument(arg, **kwargs)
    args = parse.parse_args()
    return args[arg]


app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/transaction', methods=['POST'])
def tmp2():
    if request.method == 'POST':
        username = request.json['username']
        return username


# @app.teardown_appcontext
# def tmp():
#     print "BYEBYE!"


if __name__ == '__main__':
    app.run('0.0.0.0', int("5000"), threaded=True)