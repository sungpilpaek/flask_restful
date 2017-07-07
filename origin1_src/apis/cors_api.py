""" Cors API Manager
    Generated with API Template Generator.

Description:
    [POST]      : Receieves actual requests and saves data.
    [OPTIONS]   : Receieves preflight requests or actual requests from
                  browsers, and returns response with CORS headers.
"""
import ast
from fields import cors_field
from parsers import cors_parser
from flask_restful import Resource, marshal_with
from common import message, exception, character_check


class Manager(Resource):
    available_options = ["POST", "OPTION"]
    preflight_cache_age = 30
    use_credentials = "true"
    separator = ","

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
        json_input = parsed_input.get("json")

        for item in json_input:
            item_dict = ast.literal_eval(item)
            username = item_dict["username"]
            input_date = item_dict["input_date"]

            if not character_check.is_valid(username):
                raise exception.SpecialCharacter()

            status = self.CorsRedisManager().insert(
                {
                    "username": username,
                    "input_date": input_date,
                    "transferred": False
                }
            )

            if status != message.TRANSACTION_OK:
                raise exception.InternalServerError()

        response_header = {
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Credentials": self.use_credentials
        }

        return "", message.STATUS_CREATED, response_header

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
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": self.preflight_cache_age
        }

        return "", message.STATUS_OK, response_header
