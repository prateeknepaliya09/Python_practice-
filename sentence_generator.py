# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 00:46:00 2016

@author: Prateek
"""

"""Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

Solution:"""

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print sentence
