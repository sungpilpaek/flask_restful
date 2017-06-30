from database import initializer, subscriber, context_manager
from common import config
import os


class TestInitSub(object):
    def get_tmp_db(self):
        abspath = os.path.dirname(os.path.abspath(__file__))
        filepath = abspath + "\\test.db"
        return filepath

    def create_tmp_db(self):
        if os.path.exists(self.get_tmp_db()):
            self.delete_tmp_db()

        config.SQLITE_PATH = "tests/test.db"
        config.ROWS_PER_API_CALL = 100

    def delete_tmp_db(self):
        os.remove(self.get_tmp_db())

    def test_initializer(self):
        self.create_tmp_db()
        init = initializer.Initializer()
        init.initialize_db_creating_schema()

        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "SELECT COUNT(USERNAME) AS CNT FROM SUBSCRIBER"
            )

            res = cur.fetchone()["CNT"]
        self.delete_tmp_db()
        assert res == 0

    def test_subscriber(self):
        self.create_tmp_db()
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

        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "SELECT USERNAME FROM SUBSCRIBER ORDER BY USERNAME"
            )
            res = []
            for row in cur:
                res.append(row["USERNAME"])

        assert res == ["id1", "id2", "id3", "id4"]

        sub.delete("id1")
        sub.delete("id3")
        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "SELECT USERNAME FROM SUBSCRIBER ORDER BY USERNAME"
            )
            res = []
            for row in cur:
                res.append(row["USERNAME"])

        assert res == ["id2", "id4"]

        sub.update("id2", "Pineapple")
        sub.update("id4", "Watermelon")
        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "SELECT NOTE FROM SUBSCRIBER ORDER BY USERNAME"
            )
            res = []
            for row in cur:
                res.append(row["NOTE"])

        assert res == ["Pineapple", "Watermelon"]

        self.delete_tmp_db()

