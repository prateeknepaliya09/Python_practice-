# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 01:25:54 2016

@author: Prateek
"""
#rename with slice
import os
import glob

os.chdir("J:/Imp/text files")
for file in glob.glob("*.json"):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    new_file_name = file_name[:-6] + extension
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(e)
    else:
        print("Renamed {} to {}".format(file, new_file_name))