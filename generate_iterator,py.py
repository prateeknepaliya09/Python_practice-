# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:54:17 2016

@author: Prateek
"""

"""Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

Solution:"""


def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print i