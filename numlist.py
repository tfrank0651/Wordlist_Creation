#!/usr/bin/env python3
# numlist.py
# Created by: Tyler Frank
# This script generates a numeric wordlist based off of user input

import sys
import itertools

# Error checking
if len(sys.argv) != 4:
    print("incorrect number of arguments. Command line args are: filepath, min length, max length")
    exit(-1)
filepath = sys.argv[1]
low = int(sys.argv[2])
high = int(sys.argv[3])

if (low < 0) or (high < 0):
    print("error, input values cannot be negative")
    exit(-1)

# create the file
f = open(filepath, "w+")

# generate all possible combinations starting with low ending on high
i = high
while i <= high:
    x = itertools.combinations_with_replacement(range(10), i)

    for tup in list(x):
        # convert tuple to string and write to file
        temp = int(''.join(map(str, tup)))
        wrStr = str(temp)
        if len(wrStr) >= low:
            f.write(str(wrStr) + '\n')
    i = i + 1
print("created and wrote attack dictionary to: " + filepath + "\n")
# close the file
f.close()