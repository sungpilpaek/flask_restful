""" Collection of predefined variables for configuration.

Attributes:
    DB_TYPE_STRING (str): Relative path to where sqlite db will be installed.
    MASTER_KEY (str): Key for encryption/decryption of indice.
    RETURN_ROWS_PER_API_CALL (int): Limit for row returns per api call.
"""
LOG_PATH = "logs/log.txt"
LOG_MAX_BYTE = 20000
LOG_BACKUP_COUNT = 5
MASTER_KEY = "7cqXx0ukQykc4BYNyGoR1SMQY20Q5MxU"
DB_TYPE_STRING = "database/example.db"
ROWS_PER_API_CALL = 2