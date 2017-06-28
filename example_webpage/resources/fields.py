from flask_restful import fields, marshal_with

SubscribersAPI_fields = {
    'username': fields.String(attribute='USERNAME'),
    'input_date': fields.String(attribute='INPUT_DATE'),
    'index': fields.String(attribute="IDX")
}