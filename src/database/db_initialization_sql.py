"""
    Collection of SQL statements

Attributes:
    CREATE_SCHEMA_1 (String)        : Creates a table and constraints for
                                      initialization
    CREATE_SCHEMA_1 (String)        : Creates a table and constraints for
                                      initialization
"""
CREATE_SCHEMA_1 = """
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
"""

CREATE_SCHEMA_2 = """
 CREATE UNIQUE INDEX IF NOT EXISTS
 USERNAME_IDX_1 ON SUBSCRIBER (USERNAME)
 ;
"""