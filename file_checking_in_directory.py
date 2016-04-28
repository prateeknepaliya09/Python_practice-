# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:04:49 2016

@author: Prateek
"""
#file checking
import os
import os.path

PATH='./file.txt'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "File exists and is readable"
else:
    print "Either file is missing or is not readable"