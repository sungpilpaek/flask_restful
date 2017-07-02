""" Output field conveniently filters unnecessary data
"""
from flask_restful import fields


http_get_field = {
    'username': fields.String(attribute='USERNAME'),
    'input_date': fields.String(attribute='INPUT_DATE')
}