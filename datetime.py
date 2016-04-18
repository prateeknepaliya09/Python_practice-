# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:49:12 2016

@author: Prateek
"""


"""dates are easily constructed and formatted"""

from datetime import date

now = date.today()
print now

datetime.date(2003, 12, 2)

print now.strftime("%m-%d-%y or %d%b %Y is a %A on the %d day of %B")


# dates support calendar arithmetic

birthday = date(1964, 7, 31)
age = now - birthday
print age.days # 14368
