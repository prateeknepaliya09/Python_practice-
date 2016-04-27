# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:01:33 2016

@author: Prateek
"""

def reverse(test):
    n = len(test)
    x=""
    for i in range(n-1,-1,-1):
        x += test[i]
    return x