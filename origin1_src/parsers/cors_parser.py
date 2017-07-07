""" Cors Parsers.
    Generated with API Template Generator.

Description:
    [fetch_httppost_input]      : Receieves CORS header, Origin and
                                  other required parameters.
    [fetch_httpoptions_input]   : Receieves CORS header for preflight
                                  request.

"""
from flask_restful import reqparse


REQPARSE_LOCATION_FORM = "form"
REQPARSE_LOCATION_QUERY_STRING = "args"
REQPARSE_LOCATION_HEADERS = "headers"
REQPARSE_LOCATION_COOKIES = "cookies"
REQPARSE_LOCATION_JSON = 'json'


class Manager(object):
    def fetch_httppost_input(self):
        httppost_parser = reqparse.RequestParser(bundle_errors=True)
        httppost_parser.add_argument(
            "Origin",
            help="Origin: {error_msg}",
            location=REQPARSE_LOCATION_HEADERS,
            required=True
        )
        httppost_parser.add_argument(
            "json",
            help="json: {error_msg}",
            location=REQPARSE_LOCATION_JSON,
            action='append',
            required=True
        )

        res = httppost_parser.parse_args()

        return res

    def fetch_httpoptions_input(self):
        httpoptions_parser = reqparse.RequestParser(bundle_errors=True)
        httpoptions_parser.add_argument(
            "Origin",
            help="Origin: {error_msg}",
            location=REQPARSE_LOCATION_HEADERS,
            required=True
        )
        
        httpoptions_parser.add_argument(
            "Access-Control-Request-Method",
            help="Access-Control-Request-Method: {error_msg}",
            location=REQPARSE_LOCATION_HEADERS
        )

        res = httpoptions_parser.parse_args()

        return res