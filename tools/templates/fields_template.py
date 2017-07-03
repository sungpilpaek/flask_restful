shell='''""" {{API_NAME_TITLE}} Fields.
    Generated with API Template Generator.

Description:
    [httpget_field]     :
    [httppost_field]    :
    [httpput_field]     :
    [httpdelete_field]  :

"""
from flask_restful import fields


httpget_field = {{
    "something": fields.String(attribute="SOMETHING")
}}

httppost_field = {{
    "something": fields.String(attribute="SOMETHING")
}}

httpput_field = {{
    "something": fields.String(attribute="SOMETHING")
}}

httpdelete_field = {{
    "something": fields.String(attribute="SOMETHING")
}}
'''