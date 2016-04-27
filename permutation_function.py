# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:57:09 2016

@author: Prateek
"""

def permute_in_place(a):
    a.sort()
    yield list(a)

    if len(a) <= 1:
        return

    first = 0
    last = len(a)
    while 1:
        i = last - 1

        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = last - 1
                while not (a[i] < a[j]):
                    j = j - 1
                a[i], a[j] = a[j], a[i] # swap the values
                r = a[i+1:last]
                r.reverse()
                a[i+1:last] = r
                yield list(a)
                break
            if i == first:
                a.reverse()
                return

if __name__ == '__main__':
    for n in range(5):
        for a in permute_in_place(range(1, n+1)):
            print a
        print

    for a in permute_in_place([0, 0, 1, 1, 1]):
        print a
    print