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
import db_{API_NAME_LOWERCASE}_sql
from common import message, exception, config


class Manager(object):
    @transaction._with(db_{API_NAME_LOWERCASE}_sql.SELECT, return_rows=True)
    def select(self, *args):
        pass

    @transaction._with(db_{API_NAME_LOWERCASE}_sql.INSERT)
    def insert(self, *args):
        return message.TRANSACTION_OK

    @transaction._with(db_{API_NAME_LOWERCASE}_sql.UPDATE)
    def update(self, *args):
        return message.TRANSACTION_OK

    @transaction._with(db_{API_NAME_LOWERCASE}_sql.DELETE)
    def delete(self, *args):
        return message.TRANSACTION_OK
'''