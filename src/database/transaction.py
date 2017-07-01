""" Implementation of ContextManager class which is designed to perform
    secured transaction of database.
"""
import sqlite3
from common import config, exception


class DatabaseWrapper(object):
    def __enter__(self):
        self.conn = sqlite3.connect(config.SQLITE_PATH)
        self.conn.row_factory = self.dict_factory
        self.cur = self.conn.cursor()

        return self

    def __exit__(self, exception_type, exception_value, traceback):
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