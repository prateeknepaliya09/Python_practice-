# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:03:51 2016

@author: Prateek
"""

import MySQLdb

# connect
db = MySQLdb.connect(host="localhost", user="appuser", passwd="",
db="onco")

cursor = db.cursor()

# execute SQL select statement
cursor.execute("SELECT * FROM LOCATION")

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time.
for x in range(0,numrows):
    row = cursor.fetchone()
    print row[0], "-->", row[1]