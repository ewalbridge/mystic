#!/usr/bin/python

import StringIO, gzip
out = StringIO.StringIO()
with gzip.GzipFile(fileobj=out, mode='w', compresslevel=9) as data:
    data.write('1234567890')
print out.getvalue()
