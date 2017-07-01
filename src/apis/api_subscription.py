""" Subscribers API

Methods:    [GET]   Returns limited rows of subscribers with an index
            [POST]  Inserts the subscriber's username into the database
"""
from fields import field_subscription
from parsers import parser_subscription
from flask_restful import Resource, marshal
from common import message, exception, security


class Manager(Resource):
    def __init__(self, **kwargs):
        self.db_manager = kwargs['db_manager']

    def get(self):
        """ Parse the inputs and filter out any unnecessary or
            dangerous parameters.
        """
        args = parser_subscription.get_parser.parse_args()

        """ AES-decryption
        """
        index = security.decryption(args['index'])

        """ Fetch the data via db_manager
        """
        res, unsafe_index, status = self.db_manager().select(index)

        """ AES-encryption
        """
        safe_index = security.encryption(unsafe_index)

        if status == message.TRANSACTION_OK:
            """ Parse the outputs filtered by flask_restful.fields.
                Didn't use @marshal_with decorator because the index
                field shouldn't be attached to every list element of
                data field. Otherwise, it will be waste of space and
                lead to a perfomance hazard!
            """
            marshaled_res = marshal(res, field_subscription.field)
            data = {'data': marshaled_res, 'index': safe_index}

            return data

        raise exception.InternalServerError()

    def post(self):
        args = parser_subscription.post_parser.parse_args()
        username = args['username']

        status = self.db_manager().insert(username)

        if status == message.TRANSACTION_OK:
            data = {'status': message.STATUS_OK, 'message': 'Success'}
            
            return data

        raise exception.InternalServerError()