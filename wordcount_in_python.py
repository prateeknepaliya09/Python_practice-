# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:48:37 2016

@author: Prateek
"""

"""Python program for word count in file."""

filename = "J:\shakes2.txt"
numLines = 0
numwords = 0
numChars = 0

with open(filename, 'r') as file:
    for line in file:
        wordsList = line.split()
        numLines += 1
        numwords += len(wordsList)
        numChars += len(line)

print "Lines: %i\nWords: %i\nCharacters: %i" % (numLines, numwords, numChars)


##############################################################################
"""
#This counts occurence of each word

file=open("J:\shakes.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v
    
#############################################################################    
fname = "J:\shakes.txt"
feed = open(fname, 'r')

num_lines = len(feed.splitlines())
num_words = 0
num_chars = 0

for line in lines:
    num_words += len(line.split())"""
    