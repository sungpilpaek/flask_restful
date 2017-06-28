from flask_restful import fields


GetSubscribers_fields = {
    'username': fields.String(attribute='USERNAME'),
    'input_date': fields.String(attribute='INPUT_DATE')
}