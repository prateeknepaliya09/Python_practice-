# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 02:32:04 2016

@author: Prateek
"""

"""Write a version of a palindrome recognizer that also accepts 
phrase palindromes such as "Go hang a salami I'm a lasagna hog.", 
"Was it a rat I saw?" Note that punctuation, capitalization, 
and spacing are usually ignored."""

import string

ignored = string.punctuation + " "

def is_palindrome1(str):
    my_str = str
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
        return True
    else:
        return False
        
###########################################################################

#optimised

def is_palindrome(str):
  cleanstr = ""
  for i in str:
    cleanstr += "" if i in ignored else i 

  return cleanstr.lower() == cleanstr[::-1].lower()

#############################################################################
  


#test
print is_palindrome("Go hang a salami I'm a lasagna hog.")
print is_palindrome("Was it a rat I saw")
print is_palindrome("Dammit, I'm mad!")
print is_palindrome1("This is not a palindrome")