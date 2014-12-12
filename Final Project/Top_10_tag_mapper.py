#!/usr/bin/python
"""
#Udacity Intro to Hadoop and MapReduce Final Project
#Top 10 tags Exercise

#This solution pass the test under this command:
cat ./forum_node.tsv | ./Top_10_tag.py | sort | ./Top_10_reducer.py

The result is 

cs101	11622
cs373	4952
cs253	4542
discussion	3560
meta	2664
cs212	2009
homework	1682
bug	1651
cs262	1561
st101	1489

HOWEVER it can't pass hadoop command:
hs ./Top_10_tag.py ./Top_10_reducer.py ./forum_node.tsv finalTag

which results in below：
cs101   6932
cs101   4690
cs253   2635
cs373   2533
cs373   2419
discussion      2414
cs253   1907
meta    1572
cs262   1460
st101   1415

For some reason the reducer will split the CS101 and CS373 count in two!!!!!!!!!!!
It took me 3 hours to debug and still got nothing!!!!!!

Update:I finally know the reason. It is because MapReduce will map the mapper into different node and different node may count different tag occurrences.In this case, there may be two node counting the same tag.

LESSON LEARNED:
Don't count anything in the mapper.Mapper only uses for selecting the information.Reducer is the one do the processsing job!!!!!!!!!!!!!!!
"""
import sys
import csv



reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

reader.next()

total=0
tag_dict={}

for line in reader:
	node_type=line[5]
	if node_type == "question":
		tags=line[2]
		tag_name=tags.split()
		for tag in tag_name:
			if tag not in tag_dict:
				tag_dict[tag]=1
			else:
				tag_dict[tag]+=1
			total+=1	

for tag in tag_dict:
	print "{0}\t{1}".format(tag,tag_dict[tag])
		