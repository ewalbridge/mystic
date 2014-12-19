import sys
import StringIO
import gzip
import io
import os
import random
import binascii
import M2Crypto
from M2Crypto import RSA, BIO
from M2Crypto.EVP import Cipher
from base64 import b64encode, b64decode

__cipher__ = 'aes_256_cbc'

#keys
class keys(object):
    def __init__(self, secret, bitsize):

        # generate the key
        rsa = RSA.gen_key(bitsize, 65537, callback=lambda x, y, z:None)
        mem = BIO.MemoryBuffer()

        # save the private key and encrypt
        rsa.save_key_bio(mem, cipher=__cipher__, callback=lambda x: self.__passphrase(secret))
        self.__prv_key = mem.read_all()
        mem.flush

        # save the public key
        rsa.save_pub_key_bio(mem)
        self.__pub_key = mem.read_all()
        mem.flush

    def __passphrase(self, secret):
        return secret

    @property
    def prv_key(self):
        return self.__prv_key

    @property
    def pub_key(self):
        return self.__pub_key

class aes_encryption_service(object):
    def aes_encrypt(self, key, msg):
        return self.__cipher(key, msg, 1)

    def aes_decrypt(self, key, msg):
        return self.__cipher(key, msg, 0)

    def __cipher(self, key, msg, op):
        iv = '\0' * 16
        iv.encode('ascii')
        cipher = M2Crypto.EVP.Cipher(alg='aes_256_cbc', key=key, iv=iv, op=op)
        v = cipher.update(msg)
        v = v + cipher.final()
        del cipher
        return v

#encrypt
class encrypt(object):
    def __init__(self, data, password, public_key):
        bio = BIO.MemoryBuffer(str(public_key).encode('utf8')) # read public key into memory
        rsa = RSA.load_pub_key_bio(bio) # load public key
        
        pwd = password
        enc = rsa.public_encrypt(pwd, RSA.pkcs1_oaep_padding) # encrypt password
        self.__encrypted_password = b64encode(enc) #enc.encode('base64') # encode password

        crypto_service = aes_encryption_service()
        cipher = b64encode(crypto_service.aes_encrypt(password, data))
        self.__data = cipher

    @property
    def encrypted_password(self):
        return self.__encrypted_password
   
    @property
    def data(self):
        return self.__data


#decrypt
class decrypt(object):
    def __init__(self, data, password, private_key, private_key_password):
        bio = BIO.MemoryBuffer(str(private_key).encode('utf8')) # read private key into memory
        rsa = RSA.load_key_bio(bio, callback=lambda x: self.__passphrase(private_key_password)) # load private key
        
        pwd = b64decode(password) # decode password
        dnc = str(rsa.private_decrypt(pwd, RSA.pkcs1_oaep_padding)) #  decrypt password
        self.__decrypted_password = dnc

        crypto_service = aes_encryption_service()
        cipher = crypto_service.aes_decrypt(dnc, b64decode(data))
        self.__data = cipher

    def __passphrase(self, secret):
        return secret

    @property
    def decrypted_password(self):
        return self.__decrypted_password
   
    @property
    def data(self):
        return self.__data

def random_password():
    length = random.randrange(491, 982) #491, 982
    return os.urandom(length)

def compress(value):
    out = gzip.zlib.compress(value, 9)
    return out

def decompress(value):
    out = gzip.zlib.decompress(value)
    return out

