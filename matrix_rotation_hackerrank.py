# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:56:00 2017

@author: Prateek
"""

import math 
#input
X,Y,R = map(int, raw_input().split())
matrix = [[int(x) for x in raw_input().split()] for y in range(X)]

levels = int(math.ceil(min(X,Y)/float(2)))
a = [[(x,y) for y in range(Y)] for x in range(X)]

gin = [[0 for y in range(Y)] for x in range(X)]
for x in range(levels):
    c = []
    a1 = a[x][x:len(a[x])-x]
    a2 = [a[i][len(a[x])-x-1] for i in range(x+1,len(a)-x)]
    a3= a[len(a)-x-1][x:len(a[0])-x-1][::-1]
    a4 = [a[i][x] for i in range(x+1,len(a)-x-1)][::-1]
    c += a1
    c += [h for h in a2 if h not in c] 
    c += [h for h in a3 if h not in c]
    c += [h for h in a4 if h not in c]
    k = [matrix[g[0]][g[1]] for g in c]
    rr = R%len(c)
    k = k[rr:] + k[:rr]
    for s in range(len(c)):
        gin[c[s][0]][c[s][1]] = k[s]
for x in gin:
    print(" ".join([str(i) for i in x]))