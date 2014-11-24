import sys
from M2Crypto import RSA, BIO

# set pass phrase to null
PASSKEY = ''

class generate(object):
    def __init__(self, secret, bitsize):
        self.__secret = secret
        self.__bitsize = bitsize
        # set pass phrase
        global PASSKEY
        PASSKEY = self.__secret

        # generate the key
        rsa = RSA.gen_key(self.__bitsize, 65537, callback=lambda x, y, z:None)
        mem = BIO.MemoryBuffer()

        # save the private key and encrypt
        rsa.save_key_bio(mem, cipher='aes_256_cbc', callback=self.__passphrase)

        # !!!set pass phrase back to null!!!
        # THIS MUST BE SET TO NULL
        PASSKEY = ''

        self.keyprv = mem.read_all()
        mem.flush

        # save the public key
        rsa.save_pub_key_bio(mem)
        self.keypub = mem.read_all()
        mem.flush

    def __passphrase(*args):
        return PASSKEY
