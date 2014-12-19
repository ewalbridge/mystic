#!/usr/bin/python

import crypto, sys, time, io, os, base64, binascii
from io import BytesIO
from base64 import b64encode

def timing(function):
    def wrap(*args):
        time1 = time.time()
        ret = function(*args)
        time2 = time.time()
        print '%s() took %0.3f milliseconds to complete...' % (function.func_name, (time2-time1) * 1000)
        print''
        return ret
    return wrap

@timing
def main():

    pub_key = open('/share/projects/development/source/mystic/opt/var/keys/eric.walbridge.pub', 'r')
    prv_key = open('/share/projects/development/source/mystic/opt/var/keys/eric.walbridge.prv', 'r')
    enc_file = open('/share/projects/development/source/mystic/opt/var/files/tmp/test.pdf', 'rb')
    dec_file = open('/share/projects/development/source/mystic/opt/var/files/tmp/test2.pdf', 'wb')
    print ''
    encrypt = crypto.encrypt(enc_file.read(), crypto.random_password(), pub_key.read())
    #print b64encode(encrypt.encrypted_password)
    #print encrypt.data
    #print ''
    decrypt = crypto.decrypt(encrypt.data, encrypt.encrypted_password, prv_key.read(), '0123456789')
    #print decrypt.decrypted_password
    #print b64encode(decrypt.data)
    dec_file.write(decrypt.data)
    print ''

    #full_path = sys.argv[1]
    #dir_path, file_name = os.path.split(full_path)
    #file, file_ext = os.path.splitext(full_path)
    
    #print ''
    #print '1. ' + full_path
    #print '2. ' + dir_path
    #print '3. ' + file_name
    #print '4. ' + file
    #print '5. ' + file_ext
    #print ''

    #z = crypto.compress('1')
    #u = crypto.decompress(z);
    #print z
    #print u

    #f = open(file_path, 'rb')
    #z = zipper.compress(f.read())
    #f = open(file_path + '.gzip', 'wb')
    #f.write(z)
    #f = open(file_path + '.gzip', 'rb')
    #z = zipper.decompress(f.read())
    #f = open(file_path + '2', 'wb')
    #f.write(z)

    #length = 4295098369 #982
    #passkey = os.urandom(length)
    
    #f = open('random', 'w')
    #f.write('1')
    
    #encoded = base64.b64encode(passkey)
    
    #f = open('random', 'r')
    #z = zipper.compress(f.read())

    #f = open('random.zip', 'w')
    #f.write(z)

    #print encoded

    #f = open('/share/projects/development/source/mystic/opt/var/files/tmp/test.zip', 'w')
    #f.write(z)
    #zipper.decompress(z)
main()
