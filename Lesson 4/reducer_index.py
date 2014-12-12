#!/usr/bin/python

# Solution from tylucaskelley in Github

import sys, csv, string

count = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisKey, thisValue = data_mapped
	
	if thisKey == "fantastically":
		print thisKey, "\t", thisValue
	
	if oldKey and oldKey != thisKey:
		if oldKey == "fantastic":
			print oldKey, "\t", count
        oldKey = thisKey
        count = 0
			
	oldKey = thisKey
	count += 1
	
if oldKey != None:
	print oldKey, "\t", count