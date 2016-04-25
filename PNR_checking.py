# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:25:11 2016

@author: Prateek
"""
#PNR checking, Indian Railway

import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep

try:
    pnr = input('Enter pnr ')
    url = 'http://www.railyatri.in/pnr-status/'+pnr
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    cs = soup.findAll('span',{'class':'arrival_span'})
    bs = soup.findAll('span',{'class':'departure'})
    pynotify.init('test')
    n = pynotify.Notification('PNR Status','Booking Satus: '+bs[1].text+'\n'+'Curent Satus: '+cs[2].text)
    n.show()
    
except requests.exceptions.ConnectionError:
    pynotify.init('test')
    n = pynotify.Notification('Connection Issue','No internet found')
    n.show()