"""
    Collection of predefined errors. Designed to return message and status
    when custom exception class is raised. Should be registered in app.py
    first.
    
"""
ERRORS = {
    'InvalidUsername': {
        'message': "Invalid user name: User name already exists or " \
        + "user name is an empty string.",
        'status': 400,
    },
    'InternalServerError': {
        'message': "Internal Server Error!",
        'status': 500,
    },
}


class InvalidUsername(Exception):
    pass


class InternalServerError(Exception):
    pass