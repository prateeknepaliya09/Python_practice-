# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 01:28:57 2016

@author: Prateek
"""
#basic email web crawler
import requests
import re

# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html)


# print the number of links in the list
print("\nFound {} links".format(len(links)))
for email in emails:
    print(email)