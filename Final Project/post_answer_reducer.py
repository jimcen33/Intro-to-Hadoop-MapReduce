#!/usr/bin/python

#Udacity Intro to Hadoop and MapReduce Final Project
#Post length and average answer length Exercise

# Import relevant modules
import sys


# Initialize the keys
count= 0
total = 0
oldID=None
oldBody=None

# For every line in the standard input...
for line in sys.stdin:
	data = line.strip().split('\t')
	 
	if len(data) != 3:
		continue
	 
	thisID,thisBody,thisAns=data
	 
	if oldID and oldID != thisID:
		print oldID,'\t',oldBody,'\t',total/float(count)
	    total=0
	    count=0
	
	oldID=thisID
	oldBody=thisBody
	count=count+1
	total+=int(thisAns)

if oldID != None:
	print oldID,'\t',oldBody,'\t',total/float(count)
	