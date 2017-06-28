""" Collection of flask_restful.fields which automatically format outputs
"""
from flask_restful import fields


GetSubscribers_fields = {
    'username': fields.String(attribute='USERNAME'),
    'input_date': fields.String(attribute='INPUT_DATE')
}