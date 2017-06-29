""" Collection of class and functions working with database
"""
from common import config, message, security
import sql_statements
import sqlite3


class Subscriber:
    """ An object that is declared when user submits new username
    
    Attributes:
        conn (TYPE): database connection object
        username (TYPE): username which user submitted
    """
    def __init__(self, username):
        self.conn = None
        self.username = username


    def connect_to_db(self):
        self.conn = sqlite3.connect(config.DB_TYPE_STRING)


    def insert_to_db(self):
        """ Insert a row into the database
        """
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            try:
                cur.execute(sql_statements.INSERT_SUBSCRIBER, [self.username])
            except sqlite3.IntegrityError:
                return message.TRANSACTION_FAIL_INTEGRITY
            self.conn.commit()

        self.conn.close()

        return message.TRANSACTION_OK


    def delete_from_db(self):
        """ Delete rows from the database
        """
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_statements.DELETE_SUBSCRIBER, [self.username])
            self.conn.commit()

        self.conn.close()

        return message.TRANSACTION_OK


    def update_the_db(self):
        """ Update rows
        """
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_statements.UPDATE_SUBSCRIBER, [self.username])
            self.conn.commit()

        self.conn.close()

        return message.TRANSACTION_OK


def initialize_db_creating_schema():
    """ Called at the beginning stage when app.py starts. Creates schema
    """
    conn = sqlite3.connect(config.DB_TYPE_STRING)
    with conn:
        cur = conn.cursor()
        for statement in sql_statements.CREATE_SCHEMA.split(";"):
            cur.execute(statement)
            conn.commit()

    conn.close()


def dict_factory(cursor, row):
    """ Override the original function for returning dictionaries
    
    Returns:
        TYPE: Dictionaries
    """
    res = {}
    for index, column in enumerate(cursor.description):
        res[column[0]] = row[index]

    return res


def query_subscribers(encrypted_index):
    """ Called by APIs when users request
        Return [config.RETURN_ROWS_PER_API_CALL] rows at a time
    
    Args:
        encrypted_index (String): The encrypted value of a last row
                                  from previous API call
    
    Returns:
        TYPE: [config.RETURN_ROWS_PER_API_CALL] rows + new encrypted value
              of a last row
    """
    res = []
    decrypted_index = -1 if encrypted_index is None or encrypted_index == '' \
        else security.decryption(encrypted_index)

    conn = sqlite3.connect(config.DB_TYPE_STRING)
    conn.row_factory = dict_factory
    with conn:
        cur = conn.execute(
            sql_statements.GET_MAX_ID_SUBSCRIBER,
            (decrypted_index, config.ROWS_PER_API_CALL)
        )

        max_id = str(cur.fetchone()["MAX"])
        new_encrypted_index = security.encryption(max_id)

        cur = conn.execute(
            sql_statements.SELECT_SUBSCRIBER,
            (decrypted_index, config.ROWS_PER_API_CALL)
        )

        for row in cur:
            res.append(row)

    conn.close()
    
    return res, new_encrypted_index, message.TRANSACTION_OK