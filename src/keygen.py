#!/usr/bin/python

import crypto, sys, time, zipper, io

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s() took %0.3f milliseconds to complete...' % (f.func_name, (time2-time1)*1000)
        print''
        return ret
    return wrap

@timing
def process():
    key_path = '../opt/var/keys/'
    username = sys.argv[1]
    secret = sys.argv[2]
    keys = crypto.keys(secret, 8192) # 1024 2048 4096 8192 16384
    print ''
    print keys.prv_key
    print keys.pub_key
    prv_file = open(key_path + username + '.prv', 'w')
    prv_file.write(keys.prv_key)
    pub_file = open(key_path + username + '.pub', 'w')
    pub_file.write(keys.pub_key)

process()
