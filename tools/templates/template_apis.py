shell = '''""" {API_NAME_TITLE} API Manager
    Generated with API Template Generator.

Description:
    [GET]       :
    [POST]      :
    [PUT]       :
    [DELETE]    :
"""
from fields import {API_NAME_LOWERCASE}_field
from parsers import {API_NAME_LOWERCASE}_parser
from flask_restful import Resource, marshal_with
from common import message, exception


class Manager(Resource):
    def __init__(self, **kwargs):
        self.{API_NAME_TITLE}DbManager = kwargs["{API_NAME_TITLE}DbManager"]

    @marshal_with({API_NAME_LOWERCASE}_field.httpget_field)
    def get(self):
        parsed_input = {API_NAME_LOWERCASE}_parser.Manager().fetch_httpget_input()
        
        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()

    @marshal_with({API_NAME_LOWERCASE}_field.httppost_field)
    def post(self):
        parsed_input = {API_NAME_LOWERCASE}_parser.Manager().fetch_httppost_input()

        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()

    @marshal_with({API_NAME_LOWERCASE}_field.httpput_field)
    def put(self):
        parsed_input = {API_NAME_LOWERCASE}_parser.Manager().fetch_httpput_input()

        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()

    @marshal_with({API_NAME_LOWERCASE}_field.httpdelete_field)
    def delete(self):
        parsed_input = {API_NAME_LOWERCASE}_parser.Manager().fetch_httpdelete_input()

        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()
'''