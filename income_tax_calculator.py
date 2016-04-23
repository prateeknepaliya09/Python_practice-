# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 01:44:41 2016

@author: Prateek
"""
#income_tax_calculator
import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
}

data = {
    'pay_rate': '10000',
    'filing_status': 'single',
    'pay_periods': 1,
    'state': 'CO',
    'year':
    '2014'
}

r = requests.post(
    'http://taxee.io/api/v1/calculate/2014',
    data=data,
    headers=headers
)

print(r.text)