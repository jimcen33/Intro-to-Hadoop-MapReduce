#!/usr/bin/python

#Extract the hits for each different file on the Web site

#Common Log Format:
#Input file Example:
#10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
#10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
#
#
#
#

import sys

for line in sys.stdin:
    if len(data) == 10:
    ip, id, user, datetime, timezone, method, path, proto, status, size = data
    fileName = path.split('/')[-1]
    print "{0}\t{1}".format(path,fileName)