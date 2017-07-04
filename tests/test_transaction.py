import pytest
import sqlite3
from database import transaction
from common import exception, config


class TestTransaction(object):
    def test_transaction1(self, db_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_fixture

        """ WHEN
        """
        with pytest.raises(exception.InvalidUsername):
            db_instance = transaction.DatabaseWrapper()
            with db_instance:
                
                """ THEN
                """
                raise sqlite3.IntegrityError()

    def test_transaction2(self, db_fixture):
        """ GIVEN
        """
        config.SQLITE_PATH = db_fixture

        """ WHEN
        """
        db_instance = transaction.DatabaseWrapper()
        with db_instance:
            cur = db_instance.query(
                "select 'What a beautiful day!' as TO_PLAY_PS4"
            )
            res = str(cur.fetchone()["TO_PLAY_PS4"])

            """ THEN
            """
            assert res == "What a beautiful day!"