import sys
import sqlite3
import sql_statements

sys.path.append('../')
from common.util import encryption, decryption

if __name__ == '__main__':
    db_type_string = "example.db"
else:
    db_type_string = "database/example.db"

RETURN_ROWS_PER_API_CALL = 2


class Subscriber:
    def __init__(self, username):
        self.conn = None
        self.username = username


    def connect_to_db(self):
        self.conn = sqlite3.connect(db_type_string)


    def insert_to_db(self):
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            try:
                cur.execute(sql_statements.INSERT_SUBSCRIBER, [self.username])
            except sqlite3.IntegrityError:
                return "INSERT_FAIL_NULL_VALUE"
            self.conn.commit()
        self.conn.close()


    def delete_from_db(self):
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_statements.DELETE_SUBSCRIBER, [self.username])
            self.conn.commit()
        self.conn.close()


    def update_the_db(self):
        self.connect_to_db()
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql_statements.UPDATE_SUBSCRIBER, [self.username])
            self.conn.commit()
        self.conn.close()


def initialize_db_creating_schema():
    conn = sqlite3.connect(db_type_string)
    with conn:
        cur = conn.cursor()
        cur.execute(sql_statements.CREATE_SCHEMA)
        conn.commit()
    conn.close()


def dict_factory(cursor, row):
    res = {}
    for index, column in enumerate(cursor.description):
        res[column[0]] = row[index]

    return res


def query_all_subscribers(Object):
    res = []
    args = Object['index']
    decrypted_index = -1 if args is None or args == '' else decryption(args)

    conn = sqlite3.connect(db_type_string)
    conn.row_factory = dict_factory
    with conn:
        cur = conn.execute(
            sql_statements.GET_MAX_ID_SUBSCRIBER,
            (decrypted_index, RETURN_ROWS_PER_API_CALL)
        )

        max_id = str(cur.fetchone()["MAX"])
        encrypted_index = encryption(max_id)

        cur = conn.execute(
            sql_statements.SELECT_SUBSCRIBER,
            (decrypted_index, RETURN_ROWS_PER_API_CALL)
        )

        for row in cur:
            row["IDX"] = encrypted_index
            res.append(row)

    conn.close()
    return res
