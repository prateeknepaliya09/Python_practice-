# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 01:11:49 2016

@author: Prateek
"""

# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialise sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")