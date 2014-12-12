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
    start=line.find("GET ")
    end=line.find("HTTP")
    hitFile=line[start+4:end]
    print "{0}\t{1}".format(fitFile,1)
