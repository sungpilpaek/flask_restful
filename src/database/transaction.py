""" Implementation of ContextManager class which is designed to perform
    secured transaction of database and convenient usage.
"""
import sqlite3
from functools import wraps
from common import config, message, exception


def _with(sql, return_rows=None):
    """ A decorator which significantly reduces amount of code written
        for database manipulation. It should be used inside the class
        because _decorator(self, *args) it self assumes there will be
        a self parameter.

    Usage:
        @_with(sql)
        def insert(self, username):
            pass
    """
    def _transaction_with(func):
        @wraps(func)
        def _decorator(self, *args):
            with DatabaseWrapper() as wrapper:
                cur = wrapper.query(sql, args)
                if return_rows is True:
                    res = cur.fetchall()
                    return res, message.TRANSACTION_OK

            return func(self, *args)

        return _decorator

    return _transaction_with


class DatabaseWrapper(object):
    def __enter__(self):
        self.conn = sqlite3.connect(config.SQLITE_PATH)
        self.conn.row_factory = self.dict_factory
        self.cur = self.conn.cursor()

        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """ Using context manager guarantees a graceful disconnection
            with database. Also all exceptions can be aggregated here
            to be handled with convenience.
        """
        self.conn.close()

        if exception_type is sqlite3.IntegrityError:
            raise exception.InvalidUsername
        
    def dict_factory(self, cur, row):
        """ Override the original row_factory with dict_factory returning
            dictionaries instead of returning lists.

            Example:
                Normal row_facoty        - [u'data1', u'data2']
                Changed to dict_factory  - {'col1': u'data1', 'col2': u'data2'}
        """
        res = {}
        for index, column in enumerate(cur.description):
            res[column[0]] = row[index]

        return res

    def query(self, *args):
        with self.conn:
            res = self.cur.execute(*args)
        
        self.conn.commit()

        return res