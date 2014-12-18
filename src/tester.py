#!/usr/bin/python
 
import M2Crypto, binascii

class AESEncryptionService(object):
    def ec(self, key, msg):
        try:
            encrypted = self.__cipher(key, msg, 1)
            return encrypted
        except:
            return 'encrypt error'

    def decrypt(self, key, msg):
        try:
            dc = self.__cipher(key, msg, 0)
            return dc
        except:
            return 'decrypt error'

    def __cipher(self, key, msg, op):
        iv = '\0' * 16
        iv.encode('ascii')
        cipher = M2Crypto.EVP.Cipher(alg='aes_256_cbc', key=key, iv=iv, op=op)
        v = cipher.update(msg)
        v = v + cipher.final()
        del cipher
        return v

password = 'asdfadfasdfasdfasdfasdf'

crypto_service = AESEncryptionService()
cipher = binascii.hexlify(crypto_service.ec(password, "hello world"))
print cipher

cipher = crypto_service.decrypt(password, binascii.unhexlify(cipher))
print cipher