#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import operator

current_word = None
current_count = 0
word = None
row =[]
result = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    row = line.split('\t')
    
    if(len(row) == 1):
        continue
 
    link = row[0]
    count = float(row[1])
	
    if(link not in result):
        result[link] = count
    else: 
        result[link] = result[link] + count


result = sorted(result.items(), key=operator.itemgetter(1), reverse = True)
for key in result:
	print(str(key[0])+" > "+str(key[1]))
	
