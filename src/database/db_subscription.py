""" Subscription manager which performs basic CRUD operations upon
    user's request.
"""
import transaction
import db_subscrition_sql
from common import message, exception, config


class Manager(object):
    """ An object that is declared when user submits new username
    """
    @transaction._with(db_subscrition_sql.INSERT)
    def insert(self, *args):
        return message.TRANSACTION_OK


    @transaction._with(db_subscrition_sql.DELETE)
    def delete(self, *args):
        return message.TRANSACTION_OK


    @transaction._with(db_subscrition_sql.UPDATE)
    def update(self, *args):
        return message.TRANSACTION_OK


    @transaction._with(
        db_subscrition_sql.GET_MAX_ID_WITH_LIMIT,
        return_rows=True
    )
    def _select_max_id(self, *args):
        pass


    @transaction._with(
        db_subscrition_sql.SELECT_WITH_LIMIT,
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
        res, status = self._select_max_id(index, config.ROWS_PER_API_CALL)
                   
        """ Maximum value of primary key will be returned to user as a new
            index just in case they want to have additional rows.
        """
        if status == message.TRANSACTION_OK:
            new_index = str(res[0]["MAX"])
        else:
            raise exception.InternalServerError

        res, status = self._select(index, config.ROWS_PER_API_CALL)

        if status == message.TRANSACTION_OK:
            return res, new_index, message.TRANSACTION_OK

        raise exception.InternalServerError