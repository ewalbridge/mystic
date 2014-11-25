import sys
from M2Crypto import RSA, BIO

class generate(object):
    def __init__(self, secret, bitsize):

        # generate the key
        rsa = RSA.gen_key(bitsize, 65537, callback=lambda x, y, z:None)
        mem = BIO.MemoryBuffer()

        # save the private key and encrypt
        rsa.save_key_bio(mem, cipher='aes_256_cbc', callback=lambda x: self.passphrase(secret))
        self.__keyprv = mem.read_all()
        mem.flush

        # save the public key
        rsa.save_pub_key_bio(mem)
        self.__keypub = mem.read_all()
        mem.flush

    def passphrase(self, secret):
        return secret

    @property
    def private_key(self):
        # Do something if you want
        return self.__keyprv

    @property
    def pubkic_key(self):
        # Do something if you want
        return self.__keypub