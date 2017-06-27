import sqlite3
import sql_statements

db_type_string = "database/example.db"


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


def query_all_subscribers():
    res = []
    conn = sqlite3.connect(db_type_string)
    with conn:
        cur = conn.execute(sql_statements.SELECT_SUBSCRIBER)
        for row in cur:
            res.append(row)
    conn.close()
    return res