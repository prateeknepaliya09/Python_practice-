# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:56:20 2016

@author: Prateek
"""

"""Write a program that maps a list of words into a list 
of integers representing the lengths of the correponding words."""

def words_length_in_list(lst):
  lenlist = [len(i) for i in lst]
  return lenlist

#test
print words_length_in_list(['Hello', 'world!'])
print words_length_in_list(['Python', 'is', 'awesome!'])
print words_length_in_list(['You', 'said', 'it', 'bro!'])