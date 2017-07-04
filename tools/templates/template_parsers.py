shell='''""" {API_NAME_TITLE} Parsers.
    Generated with API Template Generator.

Description:
    [fetch_httpget_input]    :
    [fetch_httppost_input]   :
    [fetch_httpput_input]    :
    [fetch_httpdelete_input] :

"""
from flask_restful import reqparse


REQPARSE_LOCATION_FORM = "form"
REQPARSE_LOCATION_QUERY_STRING = "args"
REQPARSE_LOCATION_HEADERS = "headers"
REQPARSE_LOCATION_COOKIES = "cookies"


class Manager(object):
    def fetch_httpget_input(self):
        httpget_parser = reqparse.RequestParser(bundle_errors=True)
        httpget_parser.add_argument(
            "something",
            help="something: {{error_msg}}",
            location=REQPARSE_LOCATION_QUERY_STRING
        )

        res = httpget_parser.parse_args()

        return res

    def fetch_httppost_input(self):
        httppost_parser = reqparse.RequestParser(bundle_errors=True)
        httppost_parser.add_argument(
            "something",
            help="something: {{error_msg}}",
            location=REQPARSE_LOCATION_QUERY_STRING
        )

        res = httppost_parser.parse_args()

        return res

    def fetch_httpput_input(self):
        httpput_parser = reqparse.RequestParser(bundle_errors=True)
        httpput_parser.add_argument(
            "something",
            help="something: {{error_msg}}",
            location=REQPARSE_LOCATION_QUERY_STRING
        )

        res = httpput_parser.parse_args()

        return res

    def fetch_httpdelete_input(self):
        httpdelete_parser = reqparse.RequestParser(bundle_errors=True)
        httpdelete_parser.add_argument(
            "something",
            help="something: {{error_msg}}",
            location=REQPARSE_LOCATION_QUERY_STRING
        )

        res = httpdelete_parser.parse_args()

        return res
'''