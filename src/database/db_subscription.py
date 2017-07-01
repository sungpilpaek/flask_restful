""" Subscriber Object performs basic CRUD operations upon user's request.
"""
import transaction
import sql_statement
from common import message, config


class Manager(object):
    """ An object that is declared when user submits new username
    """
    @transaction._with(sql_statement.INSERT_SUBSCRIBER)
    def insert(self, username):
        return message.TRANSACTION_OK


    @transaction._with(sql_statement.DELETE_SUBSCRIBER)
    def delete(self, username):
        return message.TRANSACTION_OK


    @transaction._with(sql_statement.UPDATE_SUBSCRIBER)
    def update(self, username, data):
        return message.TRANSACTION_OK


    @transaction._with(
        sql_statement.GET_MAX_ID_SUBSCRIBER,
        return_rows=True
    )
    def _select_max_id(self, *args):
        pass


    @transaction._with(
        sql_statement.SELECT_SUBSCRIBER,
        return_rows=True
    )
    def _select(self, *args):
        pass


    def select(self, index):
        """ For most service apis in the world, they don't return all rows at
            a time. They return limited amount of data and require additional
            api calls. This select function also returns only designated amount
            : config.ROWS_PER_API_CALL. When user requests with a proper index,
            api will return data "after" that index.
        """
        res = self._select_max_id(index, config.ROWS_PER_API_CALL)
                   
        """ Maximum value of primary key will be returned to user as a new
            index just in case they want to have additional rows.
        """
        new_index = str(res[0]["MAX"])

        res = self._select(index, config.ROWS_PER_API_CALL)

        return res, new_index, message.TRANSACTION_OK