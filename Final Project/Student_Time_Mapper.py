#!/usr/bin/python
import sys, csv, string

#Udacity Intro to Hadoop and MapReduce Final Project
#Student Time Exercise


reader = csv.reader(sys.stdin, delimiter='\t')
#specials = ',.!?:;"()<>[]#$=-/'
#trans = string.maketrans(specials, ' '*len(specials))
reader.next()

for line in reader:
	if len(line) == 19:
		hour = int(line[8][11:13])
		author_id = line[3]
		print "{0}\t{1}".format(author_id, hour)
