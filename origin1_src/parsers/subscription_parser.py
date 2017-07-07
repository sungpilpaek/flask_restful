"""
    Collection of parsers for defining/restricting users' input parameters.
    BEWARE THAT REQPARSE RETURNS DICTIONARY!

Attributes:
    GetSubscribers_parser (reqparer)        : Parser associated with
                                              GetSubscribers API
    PostSubscribers_parser (reqparer)       : Parser associated with
                                              PostSubscriber API
    REQPARSE_LOCATION_COOKIES (String)      : Parser will look for COOKIES
    REQPARSE_LOCATION_FORM (String)         : Parser will look for POST
    REQPARSE_LOCATION_HEADERS (String)      : Parser will look for HEADERS
    REQPARSE_LOCATION_QUERY_STRING (String) : Parser will look for QUERYSTING

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
            "index",
            help="The index: {error_msg}",
            location=REQPARSE_LOCATION_QUERY_STRING,
        )

        res = httpget_parser.parse_args()

        return res

    def fetch_httppost_input(self):
        httppost_parser = reqparse.RequestParser(bundle_errors=True)
        httppost_parser.add_argument(
            "username",
            help="The username: {error_msg}",
            required=True,
            location=REQPARSE_LOCATION_FORM
        )

        res = httppost_parser.parse_args()

        return res