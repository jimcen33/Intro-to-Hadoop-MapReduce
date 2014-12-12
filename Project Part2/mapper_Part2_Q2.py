#!/usr/bin/python

#Write a MapReduce program which determines the number of hits to
#the site made by each different IP address.



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
    end=line.find(" - - ")
    IPhit=line[:end]
    print "{0}\t{1}".format(IPhit,1)
