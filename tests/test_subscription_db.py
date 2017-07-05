from common import config, message
from database import transaction, subscription_db

tmp_db_path = ""


class TestSubscriptionDb(object):
    def test_subscription_db1(self, app_empty_fixture, db_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_fixture
        config.ROWS_PER_API_CALL = 10

        with app_empty_fixture.app_context():
            manager = subscription_db.Manager()
            manager.insert("id1")
            manager.insert("id2")
            manager.insert("id3")
            manager.insert("id4")

            """ WHEN
            """
            res = []
            manager = subscription_db.Manager()
            tmp0, tmp1, tmp2 = manager.select("-1")
            for item in tmp0:
                res.append(item["USERNAME"])

            """ THEN
            """
            assert res == ["id1", "id2", "id3", "id4"]

    def test_subscription_db2(self, app_empty_fixture, db_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_fixture
        config.ROWS_PER_API_CALL = 10

        """ WHEN
        """
        with app_empty_fixture.app_context():
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

    def test_subscription_db3(self, app_empty_fixture, db_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_fixture
        config.ROWS_PER_API_CALL = 10

        """ WHEN
        """
        with app_empty_fixture.app_context():
            manager = subscription_db.Manager()
            manager.delete("id1")
            manager.delete("id3")

            res = []
            tmp0, tmp1, tmp2 = manager.select("-1")
            for item in tmp0:
                res.append(item["USERNAME"])

            """ THEN
            """
            assert res == ["id2", "id4"]

    def test_subscription_db4(self, app_empty_fixture, db_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_fixture
        config.ROWS_PER_API_CALL = 10

        """ WHEN
        """
        with app_empty_fixture.app_context():
            manager = subscription_db.Manager()
            manager.update("Pineapple", "id2")
            manager.update("Watermelon", "id4")

            res = []
            tmp0, tmp1, tmp2 = manager.select("-1")
            for item in tmp0:
                res.append(item["NOTE"])

            """ THEN
            """
            assert res == ["Pineapple", "Watermelon"]