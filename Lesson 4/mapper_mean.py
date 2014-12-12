#!/usr/bin/python

from datetime import datetime

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements  weekday and cost to find outputs mean of sales for each weekday
 
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)

