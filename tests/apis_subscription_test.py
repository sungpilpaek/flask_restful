import json
import pytest
from flask import Flask
from flask_restful import Api
from common import config, security
from database import db_subscription


class TestSubscriptionsAPI(object):
    def insert_row(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        manager = db_subscription.Manager()
        manager.insert('SungPilPaek')

    def test_subscriptions_api1(self, tmp_db, tmp_app):
        config.ROWS_PER_API_CALL = 1
        self.insert_row(tmp_db)

        resp = tmp_app.get('/pizza')
        resp_dict = json.loads(resp.data.decode())
        assert '200 OK' == resp.status
        assert 'SungPilPaek' == resp_dict['data'][0]['username']
        assert security.encryption('1') == resp_dict['index']

    def test_subscriptions_api2(self, tmp_db, tmp_app):
        config.ROWS_PER_API_CALL = 1
        resp = tmp_app.post('/pizza')
        assert '400 BAD REQUEST' == resp.status

    def test_subscriptions_api3(self, tmp_db, tmp_app):
        config.ROWS_PER_API_CALL = 1
        resp = tmp_app.post('/pizza', data={'username': 'Lizzzard'})
        resp_dict = json.loads(resp.data.decode())
        assert '200 OK' == resp.status
        assert "Success" == resp_dict["message"]

    def test_subscriptions_api4(self, tmp_db, tmp_app):
        config.ROWS_PER_API_CALL = 1
        resp = tmp_app.get('/pizza')
        resp_dict = json.loads(resp.data.decode())
        assert '200 OK' == resp.status
        assert 'SungPilPaek' == resp_dict['data'][0]['username']
        with pytest.raises(IndexError):
            assert 'Lizzzard' == resp_dict['data'][1]['username']

        resp = tmp_app.get('/pizza?index=' + resp_dict['index'])
        resp_dict = json.loads(resp.data.decode())
        assert '200 OK' == resp.status
        assert 'Lizzzard' == resp_dict['data'][0]['username']