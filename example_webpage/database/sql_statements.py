"""
    Collection of SQL statements

Attributes:
    CREATE_SCHEMA (String)          : Creates a table and constraints for
                                      initialization
    DELETE_SUBSCRIBER (String)      : Delete rows that matches username
    GET_MAX_ID_SUBSCRIBER (String)  : Get max(id) with range using limit
    INSERT_SUBSCRIBER (String)      : Insert row which username is not empty
                                      string and is unique
    SELECT_SUBSCRIBER (String)      : Select rows with limit
    UPDATE_SUBSCRIBER (String)      : Update rows that matches username

"""
SELECT_SUBSCRIBER = """
 SELECT ID AS IDX, USERNAME, NOTE, INPUT_DATE, UPDATE_DATE
 FROM SUBSCRIBER
 WHERE ID > ?
 ORDER BY ID ASC
 LIMIT ?
 ;
"""

GET_MAX_ID_SUBSCRIBER = """
 SELECT MAX(ID) as 'MAX'
 FROM (SELECT ID FROM SUBSCRIBER WHERE ID > ? ORDER BY ID ASC LIMIT ?)
 ;
"""


INSERT_SUBSCRIBER = """
 INSERT INTO SUBSCRIBER
 (USERNAME, INPUT_DATE)
 VALUES (?, DATETIME('NOW','LOCALTIME'))
 ;
"""

UPDATE_SUBSCRIBER = """
 UPDATE SUBSCRIBER
 SET NOTE = ?, UPDATE_DATE = DATETIME('NOW','LOCALTIME')
 WHERE USERNAME = ?
 ;
"""

DELETE_SUBSCRIBER = """
 DELETE FROM SUBSCRIBER
 WHERE USERNAME = ?
 ;
"""

CREATE_SCHEMA = """
 CREATE TABLE IF NOT EXISTS
 SUBSCRIBER (
 ID INTEGER PRIMARY KEY AUTOINCREMENT,
 USERNAME TEXT NOT NULL,
 NOTE TEXT,
 INPUT_DATE DATE,
 UPDATE_DATE DATE,
 CONSTRAINT username_unique UNIQUE (USERNAME)
 CONSTRAINT username_check CHECK(USERNAME <> ''))
 ;

 CREATE UNIQUE INDEX IF NOT EXISTS
 USERNAME_IDX_1 ON SUBSCRIBER (USERNAME)
 ;
"""