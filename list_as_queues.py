# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:34:36 2016

@author: Prateek
"""
"""list as queues"""

#! python

# Using Lists as Queues

queue = ["Eric", "John", "Michael"]
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print queue

s=queue.pop(0)
print s

s=queue.pop(0)
print s

print queue
