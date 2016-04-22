# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 01:37:55 2016

@author: Prateek
"""
#send sms 
"""
Supported international carriers (/intl): 
Chennai RPG Cellular, Chennai Skycell / Airtel, Comviq, DT T-Mobile,
 Delhi Aritel, Delhi Hutch, Dutchtone / Orange-NL, EMT, Escotel, German T-Mobile,
 Goa BPLMobil, Golden Telecom, Gujarat Celforce, Iusacell Mexico, JSM Tele-Page,
 Kerala Escotel, Kolkata Airtel, Kyivstar, LMT, Lauttamus Communication, 
 Maharashtra BPL Mobile, Maharashtra Idea Cellular, Manitoba Telecom Systems, 
 Meteor, MiWorld, Mobileone, Mobilfone, Mobility Bermuda, Mobistar Belgium, 
 Mobitel Tanzania, Mobtel Srbija, Movistar, Mumbai BPL Mobile, Netcom, 
 Nextel Mexico, Ntelos, O2, O2 (M-mail), One Connect Austria, OnlineBeep,
 Optus Mobile, Orange, Orange Mumbai, Orange NL / Dutchtone, Oskar, 
 P&T Luxembourg, Personal Communication, Pondicherry BPL Mobile, Primtel, 
 SCS-900, SFR France, Safaricom, Satelindo GSM, Simple Freedom, Smart Telecom, 
 Southern LINC, Sunrise Mobile, Surewest Communications, Swisscom, Telcel Mexico,
 T-Mobile Austria, T-Mobile Germany, T-Mobile UK, TIM, TSR Wireless, 
 Tamil Nadu BPL Mobile, Tele2 Latvia, Telefonica Movistar, Telenor, Teletouch, Telia Denmark, UMC, Uraltel, Uttar Pradesh Escotel, Vessotel, Vodafone Italy, Vodafone Japan, Vodafone UK, Wyndtell - See more at: http://textbelt.com/#sthash.qKz8OybI.dpuf

"""
import requests

message = raw_input('Enter a Message: ')
number = raw_input('Enter the phone number: ')


payload = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/intl", data=payload)
if r.json()['success']:
    print('Success!')
else:
    print('Error!')