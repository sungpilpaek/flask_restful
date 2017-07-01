""" Subscribers API

Methods:    [GET]   Returns limited rows of subscribers with an index
            [POST]  Inserts the subscriber's username into the database
"""
from fields import field_subscrption
from parsers import parser_subscription
from flask_restful import Resource, marshal
from common import message, exception, security


class Manager(Resource):
    def __init__(self, **kwargs):
        self.db_manager = kwargs['db_manager']

    def get(self):
        args = parser_subscription.get_parser.parse_args()
        index = security.decryption(args['index'])

        res, unsafe_index, status = self.db_manager().select(index)
        safe_index = security.encryption(unsafe_index)

        if status == message.TRANSACTION_OK:
            marshaled_res = marshal(res, field_subscrption.field)
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

        elif status == message.TRANSACTION_FAIL_INTEGRITY:
            raise exception.InvalidUsername()

        raise exception.InternalServerError()