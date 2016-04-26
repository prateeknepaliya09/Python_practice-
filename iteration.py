# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:53:14 2016

@author: Prateek
"""

from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)