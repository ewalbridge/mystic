#!/usr/bin/python
 
import M2Crypto
import binascii
import sys
 
mode = sys.argv[1]
key = sys.argv[2]
data = sys.argv[3]
 
def get_cryptor(op, key, alg='aes_256_cbc', iv=None):
    if iv == None:
        iv = '\0' * 16
    cryptor = M2Crypto.EVP.Cipher(alg=alg, key=key, iv=iv, op=op)
    return cryptor
 
def encrypt(key, plaintext):
    cryptor = get_cryptor(1, key)
    ret = cryptor.update(plaintext)
    ret = ret + cryptor.final()
    ret = binascii.hexlify(ret)
    return ret
 
def decrypt(key, ciphertext):
    cryptor = get_cryptor(0, key)
    ciphertext = binascii.unhexlify(ciphertext)
    ret = cryptor.update(ciphertext)
    ret = ret + cryptor.final()
    return ret
 
if mode == 'ENC':
    print encrypt(key, data)
elif mode == 'DEC':
    print decrypt(key, data)
else:
    sys.exit(1)