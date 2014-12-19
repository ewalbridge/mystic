#!/usr/bin/python
 
import M2Crypto, binascii

class AESEncryptionService(object):
    def ec(self, key, msg):
        try:
            encrypted = self.__cipher(key, msg, 1)
            return encrypted
        except:
            return 'encrypt error'

    def dc(self, key, msg):
        try:
            decrypted = self.__cipher(key, msg, 0)
            return decrypted
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

password = binascii.hexlify('password')

crypto_service = AESEncryptionService()

cipher = crypto_service.ec(password, 'hello world')
print cipher
cipher = crypto_service.dc(password, cipher)
print cipher