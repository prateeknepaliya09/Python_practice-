# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:16:29 2016

@author: Prateek
"""

"""Using the higher order function filter(), define a function 
filter_long_words() that takes a list of words and an integer n 
and returns the list of words that are longer than n."""

def filter_long_words(words, n):
  return filter(lambda x: len(x) > n, words)

#test
print filter_long_words(['that', ' was', 'not', 'funny', 'atttttt', 'all'], 3)
