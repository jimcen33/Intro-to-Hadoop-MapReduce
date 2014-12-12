#!/usr/bin/python

import sys

totalHits=0
oldKey=None
#Count the number of hits for each different file on the Web site

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNum = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalHits
        totalHits = 0

    oldKey = thisKey
    totalHits += float(thisNum)

if oldKey != None:
    print oldKey, "\t", totalHits
