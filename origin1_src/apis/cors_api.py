""" Cors API Manager
    Generated with API Template Generator.

Description:
    [POST]      : Receieves actual requests and saves data.
    [OPTIONS]   : Receieves preflight requests or actual requests from
                  browsers, and returns response with CORS headers.
"""
from fields import cors_field
from parsers import cors_parser
from common import message, exception
from flask_restful import Resource, marshal_with


class Manager(Resource):
    available_options = ["POST", "OPTION"]
    preflight_cache_age = 30
    use_credentials = True

    def __init__(self, **kwargs):
        self.CorsRedisManager = kwargs["CorsRedisManager"]

    @marshal_with(cors_field.httpget_field)
    def get(self):
        result, status = self.CorsRedisManager().select_all()

        if status == message.TRANSACTION_OK:
            return result, message.STATUS_OK

    def post(self):
        parsed_input = cors_parser.Manager().fetch_httppost_input()
        origin = parsed_input.get("Origin")
        username = parsed_input.get("username")
        input_date = parsed_input.get("input_date")

        status = self.CorsRedisManager().insert(
            {
                "username": username, "input_date": input_date
            }
        )

        if status == message.TRANSACTION_OK:
            response_header = {
                "Access-Control-Allow-Origin": origin,
                "Access-Control-Allow-Credentials": self.use_credentials
            }

            return "", message.STATUS_OK, response_header

        raise exception.InternalServerError()

    def options(self):
        parsed_input = cors_parser.Manager().fetch_httpoptions_input()
        origin = parsed_input.get("Origin")
        acrm = parsed_input.get("Access-Control-Request-Method")
        if not acrm:
            """ This is an actual request
            """
            response_header = {
                "Allow": ",".join(self.available_options)
            }

            return "", message.STATUS_OK, response_header

        """ This is a preflight request
        """
        if acrm not in self.available_options:
            return message.STATUS_BAD_REQUEST

        response_header = {
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Credentials": self.use_credentials,
            "Access-Control-Allow-Methods": ",".join(self.available_options),
            "Access-Control-Max-Age": self.preflight_cache_age
        }

        return "", message.STATUS_OK, response_header
