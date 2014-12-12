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
import csv



reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()


for line in reader:
	node_type=line[5]
	node_id=line[0]
	question_id=str(line[7])
	author_id = line[3]
	
	#if the post is a question, save in the question dictionary, key=node_id,value=question length
	if node_type=="question":
		print "{0}\t{1}".format(node_id,author_id)
	
	#if the post is an answer, save in the answer dictionary, key=question id,value=answer length
	else:
		print "{0}\t{1}".format(question_id,author_id)
			
			
			
			
			
			