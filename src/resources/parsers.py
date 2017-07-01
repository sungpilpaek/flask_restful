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


REQPARSE_LOCATION_FORM = 'form'
REQPARSE_LOCATION_QUERY_STRING = 'args'
REQPARSE_LOCATION_HEADERS = 'headers'
REQPARSE_LOCATION_COOKIES = 'cookies'

GetSubscribers_parser = reqparse.RequestParser(bundle_errors=True)
GetSubscribers_parser.add_argument(
    'index',
    help='The index: {error_msg}',
    location=REQPARSE_LOCATION_QUERY_STRING
)

PostSubscribers_parser = reqparse.RequestParser(bundle_errors=True)
PostSubscribers_parser.add_argument(
    'username',
    help='The username: {error_msg}',
    required=True,
    location=REQPARSE_LOCATION_FORM
)