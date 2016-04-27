# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:55:28 2016

@author: Prateek
"""

def permutations(head, tail=''):
    if len(head) == 0: print tail
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])