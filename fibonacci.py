# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:30:58 2016

@author: Prateek
"""
"""Fibonacci Series"""
#! python

# Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b
 
# Now call the function we just defined:
fib(2000)
