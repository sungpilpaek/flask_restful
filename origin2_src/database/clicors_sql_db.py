"""
    Collection of SQL statements

Attributes:
    DELETE (String)                 : Delete rows that matches username
    GET_MAX_ID_WITH_LIMIT (String)  : Get max(id) with range using limit
    INSERT (String)                 : Insert row which username is not empty
                                      string and is unique
    UPDATE (String)                 : Update rows that matches username

"""
SELECT_WITH_LIMIT = """
 SELECT USERNAME, INPUT_DATE
 FROM CLICORS
 WHERE ID > ?
 AND TRANSFERRED = 0
 ORDER BY ID ASC
 LIMIT ?
 ;
"""

GET_MAX_ID_WITH_LIMIT = """
 SELECT MAX(ID) as 'MAX'
 FROM (SELECT ID FROM CLICORS WHERE ID > ? ORDER BY ID ASC LIMIT ?)
 ;
"""


INSERT = """
 INSERT INTO CLICORS
 (USERNAME, INPUT_DATE, TRANSFERRED)
 VALUES (?, DATETIME('NOW','LOCALTIME'), 0)
 ;
"""

UPDATE = """
 UPDATE CLICORS
 SET TRANSFERRED = ?, UPDATE_DATE = DATETIME('NOW','LOCALTIME')
 WHERE USERNAME = ?
 ;
"""