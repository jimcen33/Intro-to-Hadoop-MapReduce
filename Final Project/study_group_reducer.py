#!/usr/bin/python

"""
#Udacity Intro to Hadoop and MapReduce Final Project
#Study Group Exercise

We might want to help students form study groups. But first we want to see if there 
are already students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a mapreduce program 
that for each forum thread (that is a question node with all it's answers and comments) 
would give us a list of students that have posted there - either asked the question, 
answered a question or added a comment. If a student posted to that thread several times, 
they should be added to that list several times as well, to indicate intensity of communication.


"""
import sys


# Initialize the keys
oldKey=None
id=[]

# For every line in the standard input...
for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data)!=2:
		continue
	
	thisKey, thisID =data
	
	if oldKey and oldKey != thisKey:
		print oldKey, "\t",id
		id=[]
	
	oldKey=thisKey
	id=id+[thisID]
	
if oldKey != None:
	print oldKey, "\t",id