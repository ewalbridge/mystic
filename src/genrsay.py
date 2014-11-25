#!/usr/bin/python

import sys
from M2Crypto import RSA, BIO

def passphrase(*args):
    return sys.argv[2]

username = sys.argv[1]
bitsize = 8192

rsa = RSA.gen_key(bitsize, 65537, callback=lambda x, y, z:None)
mem = BIO.MemoryBuffer()

rsa.save_key_bio(mem, cipher='aes_256_cbc', callback=passphrase)
keyprv = mem.read_all()
mem.flush

rsa.save_pub_key_bio(mem)
keypub = mem.read_all()
mem.flush

file = open(username + '.prv', 'w')
file.write(keyprv)
file.close()

file = open(username + '.pub', 'w')
file.write(keypub)
file.close()

print ""
print keyprv
print keypub

