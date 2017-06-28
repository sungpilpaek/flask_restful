""" Collection of parsers that define a format of users' http request
"""
from common import util
from flask_restful import reqparse


GetSubscribers_parser = reqparse.RequestParser(bundle_errors=True)
GetSubscribers_parser.add_argument(
    'index',
    help='The index: {error_msg}',
    location=util.REQPARSE_LOCATION_QUERY_STRING
)

PostSubscribers_parser = reqparse.RequestParser(bundle_errors=True)
PostSubscribers_parser.add_argument(
    'username',
    help='The username: {error_msg}',
    required=True,
    location=[util.REQPARSE_LOCATION_FORM]
)