shell = '''""" {API_NAME_TITLE} API Manager
    Generated with API Template Generator.

Description:
    [GET]       :
    [POST]      :
    [PUT]       :
    [DELETE]    :
"""
from fields import field_{API_NAME_LOWERCASE}
from parsers import parser_{API_NAME_LOWERCASE}
from flask_restful import Resource, marshal_with
from common import message, exception


class Manager(Resource):
    def __init__(self, **kwargs):
        self.Db{API_NAME_TITLE}Manager = kwargs["Db{API_NAME_TITLE}Manager"]

    @marshal_with(field_{API_NAME_LOWERCASE}.httpget_field)
    def get(self):
        parsed_input = parser_{API_NAME_LOWERCASE}.Manager().fetch_httpget_input()
        
        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()

    @marshal_with(field_{API_NAME_LOWERCASE}.httppost_field)
    def post(self):
        parsed_input = parser_{API_NAME_LOWERCASE}.Manager().fetch_httppost_input()

        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()

    @marshal_with(field_{API_NAME_LOWERCASE}.httpput_field)
    def put(self):
        parsed_input = parser_{API_NAME_LOWERCASE}.Manager().fetch_httpput_input()

        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()

    @marshal_with(field_{API_NAME_LOWERCASE}.httpdelete_field)
    def delete(self):
        parsed_input = parser_{API_NAME_LOWERCASE}.Manager().fetch_httpdelete_input()

        """ Not implemented
        """

        if status == message.TRANSACTION_OK:
            pass

        raise exception.InternalServerError()
'''