"""
    Collection of return messages for visual aids.

Attributes:
    STATUS_BAD_REQUEST (int)            : Http response
    STATUS_CREATED (int)                : Http response
    STATUS_FORBIDDEN (int)              : Http response
    STATUS_INTERNAL_SERVER_ERROR (int)  : Http response
    STATUS_NO_CONTENT (int)             : Http response
    STATUS_NOT_AUTHORIZED (int)         : Http response
    STATUS_NOT_FOUND (int)              : Http response
    STATUS_NOT_MODIFIED (int)           : Http response
    STATUS_OK (int)                     : Http response
    TRANSACTION_FAIL_INTEGRITY (int)    : Transaction failure
    TRANSACTION_OK (int)                : Transaction succeeded

Deleted Attributes:
    REQPARSE_LOCATION_COOKIES (str)     : Moved to resources.parsers module
    REQPARSE_LOCATION_FORM (str)        : Moved to resources.parsers module
    REQPARSE_LOCATION_HEADERS (str)     : Moved to resources.parsers module
    REQPARSE_LOCATION_QUERY_STRING (str): Moved to resources.parsers module
    RETURN_ROWS_PER_API_CALL (int)      : Moved to common.config module
    
"""
STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NO_CONTENT = 204
STATUS_NOT_MODIFIED = 304
STATUS_BAD_REQUEST = 400
STATUS_NOT_AUTHORIZED = 401
STATUS_FORBIDDEN = 403
STATUS_NOT_FOUND = 404
STATUS_INTERNAL_SERVER_ERROR = 500

TRANSACTION_OK = 0x00
TRANSACTION_FAIL_INTEGRITY = 0x10