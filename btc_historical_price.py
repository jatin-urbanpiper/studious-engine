#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:28:23 2020

@author: jatinmitruka
"""

import requests
import csv
import json

#url = "https://rest.coinapi.io/v1/ohlcv/BTC/USD/history?period_id=20MIN&time_start=2017-01-01T16:45:00&time_end=2020-05-07T00:00:00&limit=100000"
#headers = {"X-CoinAPI-Key" :"C754D303-F2CA-4D1A-910E-4D574C9BE973"}
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=9TBMGY2XJE2KRT5U"
headers = {}
response = requests.get(url, headers=headers)
print(response.text)
response_data = json.loads(response.text)["Time Series (5min)"]


with open('BAJAJFINSV_price.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    header = (
                'Date',
                'Open',
                'High',
                'Low',
                'Close',
                'Volume'
            )
    writer.writerow(header)
    
    for key in response_data.keys():
        data = response_data[key]
        row = (
                key,
                data["1. open"],
                data["2. high"],
                data["3. low"],
                data["4. close"],
                data["5. volume"]
                )
        writer.writerow(row)
    '''
    for data in response_data:
        row = (
                data["time_period_end"],
                data["price_open"],
                data["price_high"],
                data["price_low"],
                data["price_close"],
                data["volume_traded"]
                )
        writer.writerow(row)
       ''' 