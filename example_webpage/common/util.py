from Crypto.Cipher import AES
import base64

master_key = "7cqXx0ukQykc4BYNyGoR1SMQY20Q5MxU"

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

REQPARSE_LOCATION_FORM = 'form'
REQPARSE_LOCATION_QUERY_STRING = 'args'
REQPARSE_LOCATION_HEADERS = 'headers'
REQPARSE_LOCATION_COOKIES = 'cookies'

RETURN_ROWS_PER_API_CALL = 2

db_type_string = "database/example.db"


def encryption(privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(master_key)
    encoded = EncodeAES(cipher, privateInfo)
    return encoded


def decryption(encryptedString):
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    encryption = encryptedString
    cipher = AES.new(master_key)
    decoded = DecodeAES(cipher, encryption)
    return decoded
