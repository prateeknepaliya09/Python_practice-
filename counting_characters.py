# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 00:42:32 2016

@author: Prateek
"""

"""Question:

Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

Solution:
"""

dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])
