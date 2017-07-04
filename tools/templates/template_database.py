shell='''""" {API_NAME_TITLE} Database Manager.
    Generated with API Template Generator.

Description:
    [select] [input]  :
             [output] :
    [insert] [input]  :
             [output] :
    [update] [input]  :
             [output] :
    [delete] [input]  :
             [output] :
"""
import transaction
import {API_NAME_LOWERCASE}_sql_db
from common import message, exception, config


class Manager(object):
    @transaction._with({API_NAME_LOWERCASE}_sql_db.SELECT, return_rows=True)
    def select(self, *args):
        pass

    @transaction._with({API_NAME_LOWERCASE}_sql_db.INSERT)
    def insert(self, *args):
        return message.TRANSACTION_OK

    @transaction._with({API_NAME_LOWERCASE}_sql_db.UPDATE)
    def update(self, *args):
        return message.TRANSACTION_OK

    @transaction._with({API_NAME_LOWERCASE}_sql_db.DELETE)
    def delete(self, *args):
        return message.TRANSACTION_OK
'''