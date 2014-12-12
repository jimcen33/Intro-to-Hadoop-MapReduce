#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    #A new list including each line and its length as a record in the form of sublist
    lineWithLength=[]
    for line in reader:
        lineWithLength.append([len(line[4]),line])
    
    #Sort lineWithLength list in descending order,pick the top 10 
    Top_N=sorted(lineWithLength,reverse=True)[0:10]
    
    #Sort the Top_N in ascending order to fit the output format
    Top_N=sorted(Top_N,reverse=False)
    
    for record in Top_N:
        writer.writerow(record[1])


#Alternative Solution

#top_n=[]
#for line in reader:
#    top_n.append(line)

#top_n=sorted(top_n,key=lambda a: int(a[4]),reverse=False)[-10 if len(top_n)>10 else -1*len(top_n):]

#for line in top_n:
#    writer.writerow(line)


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

main()

