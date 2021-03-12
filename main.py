import pandas_datareader as web
import matplotlib.pyplot as plt 
import mplfinance as mpf 
import datetime as dt 

crypto = 'BTC'
currency = 'USD'

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

data = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
#print(data)

mpf.plot(data,type="candle", style="yahoo", volume=True)
