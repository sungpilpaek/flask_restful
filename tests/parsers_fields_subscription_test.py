import json
import pytest


class TestParsersFieldsSubscription(object):
    def test_parser(self, tmp_app2):
        """ GIVEN
        """
        """ tmp_app2 """

        """ WHEN
        """
        resp = tmp_app2.get("/very/scary/hello/machine/?index=228&abc=def")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "200 OK" == resp.status
        assert "228" == resp_dict["index"]
        with pytest.raises(KeyError):
            assert 1 == resp_dict["abc"]

    def test_field(self, tmp_app2):
        """ GIVEN
        """
        """ tmp_app2 """

        """ WHEN
        """
        resp = tmp_app2.post("/very/scary/hello/machine/")
        resp_dict = json.loads(resp.data.decode())

        """ THEN
        """
        assert "At the time when I had 99 tacos." == resp_dict["input_date"]
        assert "SungPilPaek" == resp_dict["username"]
        with pytest.raises(KeyError):
            assert "Nice to meet you!!" == resp_dict["Hello!!"]