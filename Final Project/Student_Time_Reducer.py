#!/usr/bin/python

#Udacity Intro to Hadoop and MapReduce Final Project
#Student Time Exercise

# Import relevant modules
import sys

hour_count=[0]*24
oldAuthor=None

for line in sys.stdin:
	data=line.strip().split('\t')
	
	if len(data) != 2:
		continue
	
	thisAuthor,thisHour = data
	
	if oldAuthor and oldAuthor != thisAuthor:
		for hour,count in enumerate(hour_count):
			if count==max(hour_count):
				print oldAuthor,"\t",hour
		hour_count=[0]*24
	
	oldAuthor = thisAuthor
	hour_count[int(thisHour)]+=1
	
if oldAuthor != None:
	for hour,count in enumerate(hour_count):
		if count==max(hour_count):
			print oldAuthor,"\t",hour