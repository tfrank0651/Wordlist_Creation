#!/usr/bin/env python3
# numlist.py
# Created by: Tyler Frank
# This script generates all possible 64-bit hex keys

import itertools
import string
import sys

if len(sys.argv) != 2:
    print("please specify filepath for output")
    exit(-1)
filepath = sys.argv[1]

# open filepath
f = open(filepath, "w+")

# generate all possible permutations
key = "1234567890abcdef"
a = string.ascii_letters
print('creating perms')
p = itertools.combinations_with_replacement(key, 16)
print('done with perms')

dic = []
for i in list(p):
    if (i not in dic):
        dic.append(i)
        print(''.join(i))
        # f.write(bytes(''.join(i)))
        # f.write(''.join(i))

print('generated all possible keys to: ' + filepath + "\n")
f.close()