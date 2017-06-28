from Crypto.Cipher import AES
import base64

master_key = "7cqXx0ukQykc4BYNyGoR1SMQY20Q5MxU"


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
