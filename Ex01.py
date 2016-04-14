# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:56:20 2016

@author: Prateek
"""

"""Write a program that maps a list of words into a list 
of integers representing the lengths of the correponding words."""

def words_length(lst):
  lenlist = [len(i) for i in lst]
  return lenlist

#test
print words_length(['Hello', 'world!'])
print words_length(['Python', 'is', 'awesome!'])
print words_length(['You', 'said', 'it', 'bro!'])