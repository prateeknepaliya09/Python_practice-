# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 01:08:20 2016

@author: Prateek
"""

# Python program to check if the input year is a leap year or not

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))