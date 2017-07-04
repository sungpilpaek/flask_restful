import json
import pytest
from common import config, security
from database import subscription_db


class TestSubscriptionApi(object):
    def insert_row(self, db_fixture):
        config.SQLITE_PATH = db_fixture
        manager = subscription_db.Manager()
        manager.insert("SungPilPaek")

    def test_subscription_api1(self, db_fixture, tmp_app):
        """ GIVEN
        """
        config.ROWS_PER_API_CALL = 1
        self.insert_row(db_fixture)

        """ WHEN
        """
        resp = tmp_app.get("/pizza")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "SungPilPaek" == resp_dict["data"][0]["username"]
        assert security.encryption("1") == resp_dict["index"]

    def test_subscription_api2(self, db_fixture, tmp_app):
        """ GIVEN
        """
        config.ROWS_PER_API_CALL = 1

        """ WHEN
        """
        resp = tmp_app.post("/pizza")

        """ THEN
        """
        assert "400 BAD REQUEST" == resp.status

    def test_subscription_api3(self, db_fixture, tmp_app):
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

    def test_subscription_api4(self, db_fixture, tmp_app):
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