import sys
from M2Crypto import RSA, BIO

class generate_keys(object):
    def __init__(self, secret, bitsize):

        # generate the key
        rsa = RSA.gen_key(bitsize, 65537, callback=lambda x, y, z:None)
        mem = BIO.MemoryBuffer()

        # save the private key and encrypt
        rsa.save_key_bio(mem, cipher='aes_256_cbc', callback=lambda x: self.__passphrase(secret))
        self.__keyprv = mem.read_all()
        mem.flush

        # save the public key
        rsa.save_pub_key_bio(mem)
        self.__keypub = mem.read_all()
        mem.flush

    def __passphrase(self, secret):
        return secret

    @property
    def prv_key(self):
        return self.__keyprv

    @property
    def pub_key(self):
        return self.__keypub
