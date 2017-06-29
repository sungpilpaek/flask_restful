"""
    Create a logger

"""
from logging.handlers import RotatingFileHandler
import logging
import config


def getLogHandler():
    handler = RotatingFileHandler(
        config.LOG_PATH,
        maxBytes=config.LOG_MAX_BYTE,
        backupCount=config.LOG_BACKUP_COUNT
    )

    formatter = logging.Formatter(
        '[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s >\n%(message)s'
    )
    
    handler.setFormatter(formatter)
    handler.setLevel(logging.WARNING)

    return handler