import pytest
import sqlite3
from database import context_manager
from common import exception, config


class TestContextManager(object):
    def test_integrityerror(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        with pytest.raises(exception.InvalidUsername):
            db_instance = context_manager.DatabaseContextManager()
            with db_instance:
                raise sqlite3.IntegrityError()

    def test_query(self, tmp_db):
        config.SQLITE_PATH = tmp_db
        db_instance = context_manager.DatabaseContextManager()
        with db_instance:
            cur = db_instance.query(
                "select 'What a beautiful day!' as TO_PLAY_PS4"
            )
            res = str(cur.fetchone()["TO_PLAY_PS4"])
            assert res == "What a beautiful day!"