#!/usr/bin/python

import crypto, sys, time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s() took %0.3f milliseconds to complete...' % (f.func_name, (time2-time1)*1000)
        #print '%s() took %0.3f seconds to complete...' % (f.func_name, (time2-time1))
        print''
        return ret
    return wrap

@timing
def process():
    x = crypto.generate(sys.argv[1], 4096)
    print ''
    print '-----BEGIN PASSKEY-----'
    print crypto.PASSKEY
    print '-----END PASSKEY-----'
    print ''
    print x.keyprv
    print x.keypub

process()