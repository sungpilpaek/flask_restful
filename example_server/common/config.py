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

DEBUG = False
LOGGING_LEVEL = logging.DEBUG
LOGGER_NAME = "AWESOME_LOG"
LOG_PATH = "logs/log.txt"
LOG_MAX_BYTE = 20000
LOG_BACKUP_COUNT = 1
MASTER_KEY = "7cqXx0ukQykc4BYNyGoR1SMQY20Q5MxU"
DB_TYPE_STRING = "database/example.db"
ROWS_PER_API_CALL = 2