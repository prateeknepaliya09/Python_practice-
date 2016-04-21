# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 01:06:21 2016

@author: Prateek
"""


# Python program to swap two variables provided by the user

x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))