# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:57:54 2016

@author: Prateek
"""

import time

def num_suffix(n):
    '''
    Returns the suffix for any given int
    '''
    suf = ('th','st', 'nd', 'rd')
    n = abs(n) # wise guy
    tens = int(str(n)[-2:])
    units = n % 10
    if tens > 10 and tens < 20:
        return suf[0] # teens with 'th'
    elif units <= 3:
        return suf[units]
    else:
        return suf[0] # 'th'

def day_suffix(t):
    '''
    Returns the suffix of the given struct_time day
    '''
    return num_suffix(t.tm_mday)

# Examples
print num_suffix(123)
print num_suffix(3431)
print num_suffix(1234)
print ''
print day_suffix(time.strptime("1 Dec 00", "%d %b %y"))
print day_suffix(time.strptime("2 Nov 01", "%d %b %y"))
print day_suffix(time.strptime("3 Oct 02", "%d %b %y"))
print day_suffix(time.strptime("4 Sep 03", "%d %b %y"))
print day_suffix(time.strptime("13 Nov 90", "%d %b %y"))
print day_suffix(time.strptime("14 Oct 10", "%d %b %y"))​​​​​​​