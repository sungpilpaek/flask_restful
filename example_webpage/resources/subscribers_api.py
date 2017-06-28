from flask_restful import Resource
from fields import *
from parsers import *


def parse_arg_from_requests(arg, **kwargs):
    parse = reqparse.RequestParser()
    parse.add_argument(arg, **kwargs)
    args = parse.parse_args()
    return args[arg]


class SubscribersAPI(Resource):
    def __init__(self, **kwargs):
        self.query_all = kwargs['query_all']

    @marshal_with(SubscribersAPI_fields)
    def get(self):
        index = SubscribersAPI_parser.parse_args()
        return self.query_all(index)
