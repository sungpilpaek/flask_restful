""" Collection of predefined variables for configuration.

Attributes:
    DB_TYPE_STRING (str):     Relative path to where sqlite db will be
                              installed.
    DEBUG (bool):             Run app.py with DEBUG/PRODUCTION mode.
    LOG_BACKUP_COUNT (int):   Number of backup logs after bytes exceeded
                              LOG_MAX_BYTE
    LOG_MAX_BYTE (int):       Maximun length of bytes that log will maintain.
    LOG_PATH (str):           Relative path to the file where logs will be
                              stored.
    LOGGER_NAME (str):        Logger name for global access to log instance.
    LOGGING_LEVEL (TYPE):     Logging level (INFO, WARNING, ERROR, DEBUG)
    MASTER_KEY (str):         Key for encryption/decryption of indice.
    ROWS_PER_API_CALL (int):  Limit for row returns per api call. (Renamed)

Deleted Attributes:
    RETURN_ROWS_PER_API_CALL (int): Limit for row returns per api call.

"""
import logging

API_SECRET_KEY = "j3.GX~y`PWHb=]|gsekLP.1-%L!9o|ASDFF1Y.tU|M3}iYq'o3Pm~2%-|lLgxAK"
DEBUG = False
LOG_BACKUP_COUNT = 1
LOG_MAX_BYTE = 20000
LOG_PATH = "logs/log.txt"
LOGGER_NAME = "AWESOME_LOG"
LOGGING_LEVEL = logging.WARNING
MASTER_KEY = "7cqXx0ukQykc4BYNyGoR1SMQY20Q5MxU"
PRESERVE_CONTEXT_ON_EXCEPTION = False
ROWS_PER_API_CALL = 2
SQLITE_PATH = "database/example.db"