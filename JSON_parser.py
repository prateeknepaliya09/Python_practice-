# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:10:48 2016

@author: Prateek
"""

import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)
pprint(data)