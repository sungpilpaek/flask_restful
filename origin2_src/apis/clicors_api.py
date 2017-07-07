""" Clicors API

Methods:    [GET]   Returns limited rows of subscribers with an index
            [POST]  Inserts the subscriber's username into the database
"""
import ast
from fields import clicors_field
from parsers import clicors_parser
from flask_restful import Resource, marshal
from common import message, exception, security, character_check


class Manager(Resource):
    separator = ","

    def __init__(self, **kwargs):
        self.ClicorsDbManager = kwargs["ClicorsDbManager"]

    def get(self):
        """ Parse the inputs and filter out any unnecessary or
            dangerous parameters.
        """
        parsed_input = clicors_parser.Manager().fetch_httpget_input()
        index = parsed_input.get("index")

        """ AES-decryption
        """
        decrypted_index = security.decryption(index)

        """ Fetch the data via clicors_db_manager
        """
        result, new_index, status = \
            self.ClicorsDbManager().select(decrypted_index)

        """ AES-encryption
        """
        encrypted_new_index = security.encryption(new_index)

        if status == message.TRANSACTION_OK:
            """ Parse the outputs filtered by flask_restful.fields.
                Didn"t use @marshal_with decorator because the index
                field shouldn"t be attached to every list element of
                data field. Otherwise, it will be waste of space and
                lead to a perfomance hazard!
            """
            marshaled_res = marshal(result, clicors_field.httpget_field)
            data = {"data": marshaled_res, "index": encrypted_new_index}

            return data, message.STATUS_OK

        raise exception.InternalServerError()

    def post(self):
        parsed_input = clicors_parser.Manager().fetch_httppost_input()
        username = parsed_input.get("username")

        if not character_check.is_valid(username):
            raise exception.SpecialCharacter()

        status = self.ClicorsDbManager().insert(username)

        if status == message.TRANSACTION_OK:
            return "", message.STATUS_CREATED

        raise exception.InternalServerError()

    def patch(self):
        parsed_input = clicors_parser.Manager().fetch_httppatch_input()
        json_input = parsed_input.get("json")
        transferred = parsed_input.get("transferred")

        for item in json_input:
            item_dict = ast.literal_eval(item)
            username = item_dict["username"]

            if not character_check.is_valid(username):
                raise exception.SpecialCharacter()

            status = self.ClicorsDbManager().update(transferred, username)

            if status != message.TRANSACTION_OK:
                raise exception.InternalServerError()
            
        return "", message.STATUS_ACCEPTED