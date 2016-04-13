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


print highestNumber ([-1,-55,-12])
##########################################################################    

"""Define a function max() that takes two numbers as arguments 
and returns the largest of them. 
Without using max() of python inbuilt"""

def max(n1, n2):
  if n1 > n2:
    return n1
  else:
    return n2

#test
print max(3, 5)
print max(10, 6)


##########################################################################   

#optimized
def returnhigh(l):
    l.sort() #SORTING
    return l[-1]  #returns last element
    

print returnhigh([77,48,19,17,93,90])   

