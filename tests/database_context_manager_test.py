import sys
sys.path.append("../")
from example_server.database import context_manager

class TestContextManager(object):
    def 

    # import requests
    # from flask import Flask, request, url_for
    # import json


    # index = ''
    # while True:
    #     res = json.loads(requests.get("http://localhost:5000/api/v1/subscribers", {'index': index}).json())
    #     index = res["index"]
    #     print res
    #     if res["data"] == []:
    #         break

    # app = Flask(__name__)
    # with app.test_request_context():
    #     print url_for('postsubscribers')

    # app = Flask(__name__)
    # with app.test_request_context('/api/v1/subscibers', method='POST'):
    #     print request.path