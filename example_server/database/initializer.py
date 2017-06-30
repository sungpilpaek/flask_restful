from common import message
import sql_statements
import context_manager


class Initializer(object):
    def __init__(self, username=None):
        self.database_instance = context_manager.DatabaseContextManager()

    def initialize_db_creating_schema(self):
        """ Called at the beginning stage when app.py starts. Creates schema
        """
        with self.database_instance:
            for statement in sql_statements.CREATE_SCHEMA.split(";"):
                self.database_instance.query(statement)

        return message.TRANSACTION_OK