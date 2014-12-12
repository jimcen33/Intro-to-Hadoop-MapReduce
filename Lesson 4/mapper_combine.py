#!/usr/bin/python

#Solution from jm-contreras in Github


# Import relevant modules
import sys
import csv

# Create a writer object
writer = csv.writer(sys.stdout, delimiter='\t')

# Skip the header...
reader.next()

# For every line in the data...
for line in csv.reader(sys.stdin, delimiter='\t'):
    # ...if it is part of forum_users, which has 5 lines
    if len(line) == 5:
    # ...write the relevant lines to the standard output
	    writer.writerow([line[0]] + ['A'] + line[1:])

    # ...if it is part of forum_node, which has 19 lines
    elif len(line) == 19:
    	# ...write the relevant lines to the standard output
	    writer.writerow([line[3]] + ['B'] + line[:3] + line[5:10])