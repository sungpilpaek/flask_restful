""" Util module used for encryption and decription.
"""
from Crypto.Cipher import AES
import base64
import config


def encryption(privateInfo):
    """ Encrypts the passed argument
    
    Args:
        privateInfo (TYPE): String(mostly) to be encrypted
    
    Returns:
        TYPE: Encrypted string
    """
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(config.MASTER_KEY)
    encoded = EncodeAES(cipher, privateInfo)

    return encoded


def decryption(encryptedString):
    """ Decrypts the passed argument
    
    """
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    encryption = encryptedString
    cipher = AES.new(config.MASTER_KEY)
    decoded = DecodeAES(cipher, encryption)
    
    return decoded
