import os
from flask import Flask
from common import config
from database import initialization_db, transaction


class TestInitializationDb(object):
    def test_initialization_db1(self, db_empty_fixture, app_empty_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_empty_fixture
        manager = initialization_db.Manager()

        with app_empty_fixture.app_context():
            manager.create_schema()

        """ WHEN
        """
        with app_empty_fixture.app_context():
            wrapper = transaction.DatabaseWrapper()
            with wrapper:
                cur = wrapper.query(
                    "SELECT COUNT(USERNAME) AS CNT FROM SUBSCRIBER"
                )

                res = cur.fetchone()["CNT"]
            
        # os.remove(config.SQLITE_PATH)

        """ THEN
        """
        assert res == 0