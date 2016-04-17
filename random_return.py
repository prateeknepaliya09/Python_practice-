# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:32:22 2016

@author: Prateek
"""

"""Random in Python"""

#! python

# random

import random

print random.choice(['apple', 'pear', 'banana'])

print random.sample(xrange(100), 10)   # sampling without replacement

print random.random()    # random float

print random.randrange(6)    # random integer chosen from range(6)
