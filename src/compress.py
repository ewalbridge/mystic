#!/usr/bin/python

import StringIO, gzip
out = StringIO.StringIO()
with gzip.GzipFile(fileobj=out, mode='w', compresslevel=9) as data:
    data.write('0123456789')
print out.getvalue()
