import os
from common import config
from database import db_initialization, db_subscription, transaction


config.ROWS_PER_API_CALL = 10


class TestInitSub(object):
    def test_initializer(self, tmpdir_factory):
        config.SQLITE_PATH = str(tmpdir_factory.mktemp('data').join('test2.db'))
        manager = db_initialization.Manager()
        manager.create_schema()

        wrapper = transaction.DatabaseWrapper()
        with wrapper:
            cur = wrapper.query(
                "SELECT COUNT(USERNAME) AS CNT FROM SUBSCRIBER"
            )

            res = cur.fetchone()["CNT"]
        
        os.remove(config.SQLITE_PATH)
        assert res == 0

    def test_subscriber1(self, tmp_db):
        config.SQLITE_PATH = tmp_db

        manager = db_subscription.Manager()
        manager.insert("id1")
        manager.insert("id2")
        manager.insert("id3")
        manager.insert("id4")

        res = []
        tmp0, tmp1, tmp2 = manager.select()
        for item in tmp0:
            res.append(item["USERNAME"])

        assert res == ["id1", "id2", "id3", "id4"]

    def test_subscriber2(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        wrapper = transaction.DatabaseWrapper()
        with wrapper:
            cur = wrapper.query(
                "SELECT USERNAME FROM SUBSCRIBER ORDER BY USERNAME"
            )
            res = []
            for row in cur:
                res.append(row["USERNAME"])

        assert res == ["id1", "id2", "id3", "id4"]

    def test_subscriber3(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        manager = db_subscription.Manager()
        manager.delete("id1")
        manager.delete("id3")

        res = []
        tmp0, tmp1, tmp2 = manager.select()
        for item in tmp0:
            res.append(item["USERNAME"])

        assert res == ["id2", "id4"]

    def test_subscriber4(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        manager = db_subscription.Manager()
        manager.update("id2", "Pineapple")
        manager.update("id4", "Watermelon")

        res = []
        tmp0, tmp1, tmp2 = manager.select()
        for item in tmp0:
            res.append(item["NOTE"])

        assert res == ["Pineapple", "Watermelon"]