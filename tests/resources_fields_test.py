import pytest
from flask import Flask, request, make_response
from flask_restful import Api
from resources import subscribers_api
from database import subscriber
from common import config
import json


def test_client():
    config.SQLITE_PATH = "example_server/database/example.db"
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        subscribers_api.Subscribers,
        '/api/v1/subscribers',
        resource_class_kwargs={
            'subscriber': subscriber.Subscriber
        },
        endpoint="subscribers"
    )

    app = app.test_client()
    resp = app.get('/api/v1/subscribers')
    resp_dict = json.loads(resp.data)

    assert 1 == resp_dict