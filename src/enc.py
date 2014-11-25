#!/usr/bin/python

import M2Crypto, os, random, string, sys, ntpath
from M2Crypto import RSA, BIO 
from base64 import b64decode 

def filepath(*args):
    return sys.argv[1]

def keypath(*args):
    return sys.argv[2]

def keyname(*args):
    return ntpath.basename(keypath())

def mastername(*args):
    return filepath() + '.[' + keyname() + '].master'

def encrypt_file(key, in_filename, out_filename, iv):
    cipher = M2Crypto.EVP.Cipher('aes_256_cbc', key, iv = 'iv', op = 1)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
          while True:
            buf = infile.read(1024)
            if not buf:
                break
            outfile.write(cipher.update(buf))
          outfile.write(cipher.final())  
          outfile.close()
        infile.close()

def decrypt_file(key, in_filename, out_filename, iv):
    cipher = M2Crypto.EVP.Cipher("aes_256_cbc", key, iv = 'iv', op = 0)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
          while True:
            buf = infile.read(1024)
            if not buf:
                break
            try:
                outfile.write(cipher.update(buf))
            except:
                print "here"
          outfile.write(cipher.final())  
          outfile.close()
        infile.close()


length = 982
passkey = os.urandom(length)

key = open(keypath() + '.pub', 'r').read() 
pubkey = str(key).encode('utf8')
bio = BIO.MemoryBuffer(pubkey)
rsa = RSA.load_pub_key_bio(bio) 
encrypted = rsa.public_encrypt(passkey, RSA.pkcs1_oaep_padding)
encrypted_pw = encrypted.encode('base64')

file = open(mastername(), 'w')
file.write(encrypted_pw)
file.close()

master = open(mastername(), 'r').read() 
key = open(keypath() + '.prv', 'r').read() 
priv_key = BIO.MemoryBuffer(key.encode('utf8')) 
key = RSA.load_key_bio(priv_key) 
decrypted_pw = key.private_decrypt(b64decode(master), RSA.pkcs1_oaep_padding)

encrypt_file(decrypted_pw, filepath(), filepath() + '.enc', '')
decrypt_file(decrypted_pw, filepath() + '.enc', filepath(), '')
