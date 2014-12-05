import StringIO, gzip, io

def compress(value):
    out = gzip.zlib.compress(value, 9)
    return out

def decompress(value):
    out = gzip.zlib.decompress(value)
    return out