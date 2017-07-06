""" Subscribers API

Methods:    [GET]   Returns limited rows of subscribers with an index
            [POST]  Inserts the subscriber's username into the database
"""
from flask import flash, make_response, redirect, url_for
from fields import subscription_field
from parsers import subscription_parser
from flask_restful import Resource, marshal
from common import message, exception, security


class Manager(Resource):
    def __init__(self, **kwargs):
        self.SubscriptionDbManager = kwargs["SubscriptionDbManager"]

    def get(self):
        """ Parse the inputs and filter out any unnecessary or
            dangerous parameters.
        """
        parsed_input = subscription_parser.Manager().fetch_httpget_input()
        index = parsed_input["index"]

        """ AES-decryption
        """
        decrypted_index = security.decryption(index)

        """ Fetch the data via subscription_db_manager
        """
        result, new_index, status = \
            self.SubscriptionDbManager().select(decrypted_index)

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
            marshaled_res = marshal(result, subscription_field.httpget_field)
            data = {"data": marshaled_res, "index": encrypted_new_index}

            return data

        raise exception.InternalServerError()

    def post(self):
        parsed_input = subscription_parser.Manager().fetch_httppost_input()
        username = parsed_input["username"]

        status = self.SubscriptionDbManager().insert(username)

        if status == message.TRANSACTION_OK:
            data = {"status": message.STATUS_OK, "message": "Success"}
            
            return data

        raise exception.InternalServerError()