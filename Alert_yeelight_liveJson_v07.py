#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas.io.json import json_normalize
from time import sleep
import requests
from datetime import datetime

import pandas as pd
import threading

interval = 1
awake = 180


def myPeriodicFunction():
    s = requests.Session()
    s.headers.update({'referer': "https://www.oref.org.il/11088-13708-he/Pakar.aspx"})
    s.headers.update({'X-Requested-With': "XMLHttpRequest"})
    s.headers.update({'content-type': 'text/html; charset=UTF-8'})
    url = "https://www.oref.org.il/WarningMessages/Alert/alerts.json"
    a = s.get(url).content
    b = a.decode('utf-8')

    global awake
    awake += 1
    if awake > 200:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Listening to Alerts. Current Time =", current_time)
        awake = 0

    if b != "":
        df = pd.read_json(b)
        message = (df.loc[df['data'].str.contains('רמת גן|גבעתיים|תל אביב|א|ה|ו|י')])

        if not message.empty:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            print(message)

            print(bulbIPs)

            from yeelight import Bulb
            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.turn_on()
                bulb.set_rgb(0, 0, 255)
            sleep(4)

            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.set_rgb(255, 0, 0)
            sleep(7)

            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.set_rgb(255, 255, 255)
            sleep(7)

            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.set_rgb(255, 0, 0)
            sleep(7)

            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.set_rgb(255, 255, 255)
            sleep(7)

            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.set_rgb(255, 0, 0)
            sleep(7)

            for ip in bulbIPs:
                bulb = Bulb(ip)
                bulb.set_rgb(255, 255, 255)
            sleep(25)

                # sleep(200)
                #for ip in bulbIPs:
                #    bulb = Bulb(ip)
                #    bulb.turn_off()
                #sleep(20)

            message = message.iloc[0:0]


def startAlertListener():
    threading.Timer(interval, startAlertListener).start()
    myPeriodicFunction()


from yeelight import discover_bulbs
bulbList = discover_bulbs()
global bulbIPs
bulbIPs = []
for x in bulbList:
    ip = x.get('ip') + ''
    bulbIPs += [ip]
if bulbIPs:
    print("Bulbs list: ")
    print(bulbIPs)
    startAlertListener()
else:
    print("No local Bulbs found ------- EXITING")

