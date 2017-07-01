import os
import pytest
import sqlite3
from flask import Flask
from apis import api_subscription
from database import db_subscription
from fields import field_subscription
from parsers import parser_subscription
from flask_restful import Api, Resource, marshal_with

tmp_db_path = ""


def tear_down():
    os.remove(tmp_db_path)


@pytest.fixture(scope="module")
def tmp_db(tmpdir_factory, request):
    """ GIVEN ONLY
    """
    path = str(tmpdir_factory.mktemp("data").join("test.db"))
    global tmp_db_path
    tmp_db_path = path
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    with conn:
        cur.execute(
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
        cur.execute(
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
def tmp_app(tmp_db):
    """ GIVEN ONLY
    """
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        api_subscription.Manager,
        "/pizza",
        resource_class_kwargs={
            "db_manager": db_subscription.Manager
        }
    )
    app = app.test_client()
    
    return app


class HelloMachine(Resource):
    def get(self):
        args = parser_subscription.get_parser.parse_args()

        return args

    @marshal_with(field_subscription.field)
    def post(self):
        data = {
            'Hello!!': 'Nice to meet you!!',
            'Hello!!!': 'Hello! Aloha!',
            'Username': 'Hello! This is not good!',
            'USERNAME': 'SungPilPaek',
            'iNpUt_DaTE': 'Hello! Hello!Hello!',
            'INPUT_DATE': 'At the time when I had 99 tacos.'
        }
        return data


@pytest.fixture(scope="module")
def tmp_app2(tmp_db):
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