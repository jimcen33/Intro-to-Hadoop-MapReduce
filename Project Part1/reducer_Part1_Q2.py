#!/usr/bin/python

import sys

oldKey=None
highestSale=0
# Loop around the data
# It will be in the format key\tval
# Where key is the product name, val is the sale amount
#
# The highest individual sale for each separate store  will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey,thisSale = data_mapped


    if oldKey and oldKey!=thisKey:
        print oldKey,"\t",highestSale
        highestSale=0

    oldKey=thisKey

    if highestSale < float(thisSale):
        highestSale =float(thisSale)

if oldKey != None:
    print oldKey,"\t",highestSale
