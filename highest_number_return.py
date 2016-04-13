# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 03:02:51 2016

@author: Prateek
"""
"""
Define a function max() that takes list as arguments 
and returns the largest from list. Without using max() of python inbuilt
"""
def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax


print highestNumber ([77,48,19,17,93,90])


"""Define a function max() that takes two numbers as arguments 
and returns the largest of them. 
Without using max() of python inbuilt"""

def max(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

#test
print max(3, 5)
print max(10, 6)


###########################################################################

def highestnumber(l):
    l.sort()
    return l[-1]
    

print highestnumber([77,48,19,17,93,90])   