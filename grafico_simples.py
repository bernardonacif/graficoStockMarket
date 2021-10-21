# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:37:06 2021

@author: Bernardo Nacif
"""

import yfinance as yf


inicio = '2021-01-01'
fim = '2021-10-18'

weg = yf.download('WEGE3.SA', start = inicio, end = fim)

weg['Adj Close'].plot();