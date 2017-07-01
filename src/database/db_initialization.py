""" Initializer creates database and table when very first or user deleted
    the database file.
"""
import transaction
import sql_statement
from common import message


class Manager(object):
    def __init__(self):
        self.wrapper = transaction.DatabaseWrapper()

    def create_schema(self):
        with self.wrapper:
            for statement in sql_statement.CREATE_SCHEMA.split(";"):
                self.wrapper.query(statement)

        return message.TRANSACTION_OK