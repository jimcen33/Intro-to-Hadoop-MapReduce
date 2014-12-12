#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
highestSale = 0
highestItem = None
# Loop around the data
# It will be in the format key\tItem\ttval
# Where key is the store name, Item is product name, val is the sale amount
#
# The highest individual sale for each separate store  will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisItem,thisSale = data_mapped
    
    #Compare which is the highest individual sale in a particular store
    if oldKey==thisKey and thisItem != oldItem:
        if highestSale < salesTotal:
            highestSale = salesTotal
            highestItem = oldItem
        salesTotal = 0

    if oldKey and oldKey != thisKey:
        print oldKey, "\t",highestItem,"\t", highestSale
        oldKey = thisKey;
        highestSale= 0
        salesTotal = 0

    oldKey = thisKey
    oldItem= thisItem
    salesTotal += float(thisSale)

if oldKey != None:
    if highestSale < salesTotal:
        highestSale = salesTotal
        highestItem = oldItem
    print oldKey, "\t",highestItem,"\t",highestSale
