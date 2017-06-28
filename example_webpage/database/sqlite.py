from common import util
import sql_statements
import sqlite3


class Subscriber:
    def __init__(self, username):
        self.conn = None
        self.username = username


    def connect_to_db(self):
        self.conn = sqlite3.connect(util.db_type_string)


    def insert_to_db(self):
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            try:
                cur.execute(sql_statements.INSERT_SUBSCRIBER, [self.username])
            except sqlite3.IntegrityError:
                return util.TRANSACTION_FAIL_INTEGRITY
            self.conn.commit()
        self.conn.close()
        return util.TRANSACTION_OK


    def delete_from_db(self):
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_statements.DELETE_SUBSCRIBER, [self.username])
            self.conn.commit()
        self.conn.close()
        return util.TRANSACTION_OK


    def update_the_db(self):
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_statements.UPDATE_SUBSCRIBER, [self.username])
            self.conn.commit()
        self.conn.close()
        return util.TRANSACTION_OK


def initialize_db_creating_schema():
    conn = sqlite3.connect(util.db_type_string)
    with conn:
        cur = conn.cursor()
        for statement in sql_statements.CREATE_SCHEMA.split(";"):
            cur.execute(statement)
            conn.commit()
    conn.close()


def dict_factory(cursor, row):
    res = {}
    for index, column in enumerate(cursor.description):
        res[column[0]] = row[index]

    return res


def query_all_subscribers(encrypted_index):
    res = []
    decrypted_index = -1 if encrypted_index is None or encrypted_index == '' \
        else util.decryption(encrypted_index)

    conn = sqlite3.connect(util.db_type_string)
    conn.row_factory = dict_factory
    with conn:
        cur = conn.execute(
            sql_statements.GET_MAX_ID_SUBSCRIBER,
            (decrypted_index, util.RETURN_ROWS_PER_API_CALL)
        )

        max_id = str(cur.fetchone()["MAX"])
        encrypted_index = util.encryption(max_id)

        cur = conn.execute(
            sql_statements.SELECT_SUBSCRIBER,
            (decrypted_index, util.RETURN_ROWS_PER_API_CALL)
        )

        for row in cur:
            res.append(row)

    conn.close()
    return res, encrypted_index, util.TRANSACTION_OK