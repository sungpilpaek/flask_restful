""" Subscriber Object performs basic CRUD operations upon user's request.
"""
import transaction
import sql_statement
from common import message, security, config


class Manager(object):
    """ An object that is declared when user submits new username
    """

    def __init__(self):
        self.wrapper = transaction.DatabaseWrapper()

    def insert(self, username):
        with self.wrapper:
            self.wrapper.query(
                sql_statement.INSERT_SUBSCRIBER,
                (username, )
            )

        return message.TRANSACTION_OK

    def delete(self, username):
        with self.wrapper:
            self.wrapper.query(
                sql_statement.DELETE_SUBSCRIBER,
                (username, )
            )

        return message.TRANSACTION_OK

    def update(self, username, data):
        with self.wrapper:
            self.wrapper.query(
                sql_statement.UPDATE_SUBSCRIBER,
                (
                    data,
                    username
                )
            )

        return message.TRANSACTION_OK

    def select(self, index):
        """ For most service apis in the world, they don't return all rows at
            a time. They return limited amount of data and require additional
            api calls. This select function also returns only designated amount
            : config.ROWS_PER_API_CALL. When user requests with a proper index,
            api will return data "after" that index.
        """
        res = []
        with self.wrapper:
            cur = self.wrapper.query(
                sql_statement.GET_MAX_ID_SUBSCRIBER,
                (
                    index,
                    config.ROWS_PER_API_CALL
                )
            )
            
            """ Maximum value of primary key will be returned to user as a new
                index just in case they want to have additional rows.
            """
            new_index = str(cur.fetchone()["MAX"])

            cur = self.wrapper.query(
                sql_statement.SELECT_SUBSCRIBER,
                (
                    index,
                    config.ROWS_PER_API_CALL
                )
            )

            for row in cur:
                res.append(row)
        
        return res, new_index, message.TRANSACTION_OK