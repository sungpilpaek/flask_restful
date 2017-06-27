from flask import Flask, render_template
from flask_restful import Api


app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', int("5000"), threaded=True)