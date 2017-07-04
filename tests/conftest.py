import os
import pytest
import sqlite3
from flask import Flask
from apis import subscription_api
from database import subscription_db
from fields import subscription_field
from parsers import subscription_parser
from flask_restful import Api, Resource, marshal_with

tmp_db_path = ""


def tear_down():
    os.remove(tmp_db_path)


@pytest.fixture(scope="module")
def db_fixture(tmpdir_factory, request):
    """ GIVEN ONLY
    """
    path = str(tmpdir_factory.mktemp("data").join("test.db"))

    global tmp_db_path
    tmp_db_path = path

    with sqlite3.connect(path) as conn:
        conn.execute(
            """
             CREATE TABLE IF NOT EXISTS
             SUBSCRIBER (
             ID INTEGER PRIMARY KEY AUTOINCREMENT,
             USERNAME TEXT NOT NULL,
             NOTE TEXT,
             INPUT_DATE DATE,
             UPDATE_DATE DATE,
             CONSTRAINT username_unique UNIQUE (USERNAME)
             CONSTRAINT username_check CHECK(USERNAME <> ''))
             ;
             """
        )
        conn.execute(
            """
             CREATE UNIQUE INDEX IF NOT EXISTS
             USERNAME_IDX_1 ON SUBSCRIBER (USERNAME)
             ;
            """
        )
    
    conn.commit()
    conn.close()

    request.addfinalizer(tear_down)

    return path


@pytest.fixture(scope="module")
def tmp_app():
    """ GIVEN ONLY
    """
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        subscription_api.Manager,
        "/pizza",
        resource_class_kwargs={
            "SubscriptionDbManager": subscription_db.Manager
        }
    )

    app = app.test_client()
    
    return app


class HelloMachine(Resource):
    def get(self):
        parsed_input = subscription_parser.Manager().fetch_httpget_input()

        return parsed_input

    @marshal_with(subscription_field.httpget_field)
    def post(self):
        """ Case Sensitive !!
        """
        data = {
            "Hello!!": "Nice to meet you!!",
            "Hello!!!": "Hello! Aloha!",
            "Username": "Hello! This is not good!",
            "USERNAME": "SungPilPaek",
            "iNpUt_DaTE": "Hello! Hello!Hello!",
            "INPUT_DATE": "At the time when I had 99 tacos."
        }
        return data


@pytest.fixture(scope="module")
def tmp_app2():
    """ GIVEN ONLY
    """
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        HelloMachine,
        "/very/scary/hello/machine/"
    )
    app = app.test_client()
    
    return app