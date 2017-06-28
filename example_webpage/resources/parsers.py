from flask_restful import reqparse

SubscribersAPI_parser = reqparse.RequestParser()
SubscribersAPI_parser.add_argument('index', help="The index")