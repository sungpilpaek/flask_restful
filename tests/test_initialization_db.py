import os
from common import config
from database import initialization_db, transaction


class TestInitializationDb(object):
    def test_initialization_db1(self, tmpdir_factory):
        """ GIVEN
        """
        config.SQLITE_PATH = str(tmpdir_factory.mktemp('data').join('test2.db'))
        manager = initialization_db.Manager()
        manager.create_schema()

        """ WHEN
        """
        wrapper = transaction.DatabaseWrapper()
        with wrapper:
            cur = wrapper.query(
                "SELECT COUNT(USERNAME) AS CNT FROM SUBSCRIBER"
            )

            res = cur.fetchone()["CNT"]
        
        os.remove(config.SQLITE_PATH)

        """ THEN
        """
        assert res == 0