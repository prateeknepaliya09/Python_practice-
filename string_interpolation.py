# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:19:43 2016

@author: Prateek
"""

#string Interpolation

from string import Template

greeting = 'Hello'
name = 'John'

print("%s %s how are you?" %(greeting, name))

print "%(greeting)s %(name)s how are you?" % locals()

print Template('$greeting $name how are you?').substitute(locals())

#For Python 3.0
#print("{greeting} {name} how are you?".format(**locals()))

