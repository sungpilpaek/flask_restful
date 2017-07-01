from database import initializer, subscriber, context_manager
from common import config
import os


config.ROWS_PER_API_CALL = 10


class TestInitSub(object):
    def test_initializer(self, tmpdir_factory):
        config.SQLITE_PATH = str(tmpdir_factory.mktemp('data').join('test2.db'))
        init = initializer.Initializer()
        init.initialize_db_creating_schema()

        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "SELECT COUNT(USERNAME) AS CNT FROM SUBSCRIBER"
            )

            res = cur.fetchone()["CNT"]
        
        os.remove(config.SQLITE_PATH)
        assert res == 0

    def test_subscriber1(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        init = initializer.Initializer()
        init.initialize_db_creating_schema()

        sub = subscriber.Subscriber()
        sub.insert("id1")
        sub.insert("id2")
        sub.insert("id3")
        sub.insert("id4")

        res = []
        tmp0, tmp1, tmp2 = sub.select()
        for item in tmp0:
            res.append(item["USERNAME"])

        assert res == ["id1", "id2", "id3", "id4"]

    def test_subscriber2(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "SELECT USERNAME FROM SUBSCRIBER ORDER BY USERNAME"
            )
            res = []
            for row in cur:
                res.append(row["USERNAME"])

        assert res == ["id1", "id2", "id3", "id4"]

    def test_subscriber3(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        sub = subscriber.Subscriber()
        sub.delete("id1")
        sub.delete("id3")

        res = []
        tmp0, tmp1, tmp2 = sub.select()
        for item in tmp0:
            res.append(item["USERNAME"])

        assert res == ["id2", "id4"]

    def test_subscriber4(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        sub = subscriber.Subscriber()
        sub.update("id2", "Pineapple")
        sub.update("id4", "Watermelon")

        res = []
        tmp0, tmp1, tmp2 = sub.select()
        for item in tmp0:
            res.append(item["NOTE"])

        assert res == ["Pineapple", "Watermelon"]