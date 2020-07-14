#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:34:00 2020

@author: jatinmitruka
"""

import pandas as pd


N = 10

data = pd.read_csv("BTC_volume.csv")

l = data["Date"].shape[0]

for n in range(N):
    Open = []
    Low = []
    High = []
    Close = []
    for i in range(l):
        if i <= n:
            Open.append(0)
            Low.append(0)
            High.append(0)
            Close.append(0)
        else:
            Open.append(data["Open"][i-n-1])
            High.append(data["High"][i-n-1])
            Low.append(data["Low"][i-n-1])
            Close.append(data["Close"][i-n-1])
    data["Open"+str(n+1)] = Open
    data["High"+str(n+1)] = High
    data["Low"+str(n+1)] = Low
    data["Close"+str(n+1)] = Close

data.to_csv('BTC_volume_updated.csv', index=False)