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

#@timing
def process():
    ####crypt = crypto.generate_keys(sys.argv[1], 1024) # 1024 2048 4096 6144 8192
    ####print ''
    #print crypt.prv_key
    #print crypt.pub_key

    b = "Eric Walbridge"

    z = zipper.compress(b)
    print z
    print zipper.decompress(z)

process()