""" Output field for formatting results to be returned.
"""
from flask_restful import fields


field = {
    'username': fields.String(attribute='USERNAME'),
    'input_date': fields.String(attribute='INPUT_DATE')
}