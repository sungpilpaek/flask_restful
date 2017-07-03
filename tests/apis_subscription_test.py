import json
import pytest
from common import config, security
from database import db_subscription


class TestSubscriptionsAPI(object):
    def insert_row(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        manager = db_subscription.Manager()
        manager.insert("SungPilPaek")

    def test_subscriptions_api1(self, tmp_db, tmp_app):
        """ GIVEN
        """
        config.ROWS_PER_API_CALL = 1
        self.insert_row(tmp_db)

        """ WHEN
        """
        resp = tmp_app.get("/pizza")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "SungPilPaek" == resp_dict["data"][0]["username"]
        assert security.encryption("1") == resp_dict["index"]

    def test_subscriptions_api2(self, tmp_db, tmp_app):
        """ GIVEN
        """
        config.ROWS_PER_API_CALL = 1

        """ WHEN
        """
        resp = tmp_app.post("/pizza")

        """ THEN
        """
        assert "400 BAD REQUEST" == resp.status

    def test_subscriptions_api3(self, tmp_db, tmp_app):
        """ GIVEN
        """
        config.ROWS_PER_API_CALL = 1

        """ WHEN
        """
        resp = tmp_app.post("/pizza", data={"username": "Lizzzard"})
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "Success" == resp_dict["message"]

    def test_subscriptions_api4(self, tmp_db, tmp_app):
        """ GIVEN
        """
        config.ROWS_PER_API_CALL = 1

        """ WHEN
        """
        resp = tmp_app.get("/pizza")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "SungPilPaek" == resp_dict["data"][0]["username"]

        """ WHEN
        """
        with pytest.raises(IndexError):

            """ THEN
            """
            assert "Lizzzard" == resp_dict["data"][1]["username"]

        """ WHEN
        """
        resp = tmp_app.get("/pizza?index=" + resp_dict["index"])
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "Lizzzard" == resp_dict["data"][0]["username"]