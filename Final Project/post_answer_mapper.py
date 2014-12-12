#!/usr/bin/python

#Udacity Intro to Hadoop and MapReduce Final Project
#Post length and average answer length Exercise

import sys, csv, string


reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

question={}
answer={}
lenList=[]

for line in reader:
	node_type=line[5]
	body=line[4]
	body_len=len(body)
	node_id=line[0]
	question_id=str(line[7])
	
	#if the post is a question, save in the question dictionary, key=node_id,value=question length
	if node_type=="question":
		question[node_id]=body_len
	
	#if the post is an answer, save in the answer dictionary, key=question id,value=answer length
	if node_type=="answer":
		if not question_id in anwer:
			answer[question_id]=[body_len]
		else:
			answer[question_id].append(body_len)
			

#print out the answer length for each question, if the question has no answer, print 0 as the answer length
for id in question:
	if not id in answer:
		print "{0}\t{1}\t{2}".format(int(id),int(question[id]),"0")
	else:
		for length in answer[id]:
			print "{0}\t{1}\t{2}".format(int(id),int(question[id]),length)
