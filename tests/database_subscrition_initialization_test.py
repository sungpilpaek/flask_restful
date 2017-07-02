import os
from common import config
from database import db_initialization, db_subscription, transaction


class TestInitSub(object):
    def test_db_initializer(self, tmpdir_factory):
        """ GIVEN
        """
        config.SQLITE_PATH = str(tmpdir_factory.mktemp('data').join('test2.db'))
        manager = db_initialization.Manager()
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

    def test_db_subscription1(self, tmp_db):
        """ GIVEN
        """
        config.SQLITE_PATH = tmp_db
        config.ROWS_PER_API_CALL = 10

        manager = db_subscription.Manager()
        manager.insert("id1")
        manager.insert("id2")
        manager.insert("id3")
        manager.insert("id4")

        """ WHEN
        """
        res = []
        manager = db_subscription.Manager()
        tmp0, tmp1, tmp2 = manager.select("-1")
        for item in tmp0:
            res.append(item["USERNAME"])

        """ THEN
        """
        assert res == ["id1", "id2", "id3", "id4"]

    def test_db_subscription2(self, tmp_db):
        """ GIVEN
        """
        config.SQLITE_PATH = tmp_db
        config.ROWS_PER_API_CALL = 10

        """ WHEN
        """
        wrapper = transaction.DatabaseWrapper()
        with wrapper:
            cur = wrapper.query(
                "SELECT USERNAME FROM SUBSCRIBER ORDER BY USERNAME"
            )
            res = []
            for row in cur:
                res.append(row["USERNAME"])

        """ THEN
        """
        assert res == ["id1", "id2", "id3", "id4"]

    def test_db_subscription3(self, tmp_db):
        """ GIVEN
        """
        config.SQLITE_PATH = tmp_db
        config.ROWS_PER_API_CALL = 10

        """ WHEN
        """
        manager = db_subscription.Manager()
        manager.delete("id1")
        manager.delete("id3")

        res = []
        tmp0, tmp1, tmp2 = manager.select("-1")
        for item in tmp0:
            res.append(item["USERNAME"])

        """ THEN
        """
        assert res == ["id2", "id4"]

    def test_db_subscription4(self, tmp_db):
        """ GIVEN
        """
        config.SQLITE_PATH = tmp_db
        config.ROWS_PER_API_CALL = 10

        """ WHEN
        """
        manager = db_subscription.Manager()
        manager.update("Pineapple", "id2")
        manager.update("Watermelon", "id4")

        res = []
        tmp0, tmp1, tmp2 = manager.select("-1")
        for item in tmp0:
            res.append(item["NOTE"])

        """ THEN
        """
        assert res == ["Pineapple", "Watermelon"]