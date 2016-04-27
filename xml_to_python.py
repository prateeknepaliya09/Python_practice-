# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:59:22 2016

@author: Prateek
"""

from lxml import objectify
from collections import defaultdict

count = defaultdict(int)

root = objectify.fromstring(text)

for item in root.bar.type:
    count[item.attrib.get("foobar")] += 1

print dict(count)