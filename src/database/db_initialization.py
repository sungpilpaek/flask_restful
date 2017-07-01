""" Initialization manager creates database and table when there isn't one
"""
import transaction
import sql_statement
from common import message, exception


class Manager(object):
    @transaction._with(sql_statement.CREATE_SCHEMA_1)
    def _create_schema_1(self):
        return message.TRANSACTION_OK

    @transaction._with(sql_statement.CREATE_SCHEMA_2)
    def _create_schema_2(self):
        return message.TRANSACTION_OK

    def create_schema(self):
        if self._create_schema_1() != message.TRANSACTION_OK:
            raise exception.InternalServerError

        if self._create_schema_2() != message.TRANSACTION_OK:
            raise exception.InternalServerError

        return message.TRANSACTION_OK