#!/usr/bin/env python
# coding: utf-8 - file

# IIQF - IntelliJ
# 
# - Jupyter
# - esc + a
# - esc +b
# - Shift + enter
# - Ctrl + enter
# - esc d
# - esc + m
# 
# first python program in IntelliJ Idea

print("IntelliJ line 1 " + "\n" + "Line 2")

str1 = "hello ... 3rd line " + "starts "

print(str1.upper() + "\n")
print(str1.title())

n1 = 23

print("n1 = ")
print(n1)

# homework May 7th
# 1- basics of intellij
# 2- check how get plugins for python
# 3- create one python project with intellij
# 4- take jupyter notebook code and write to one .py file and create and run
# 5- how to see plotted graph in IntelliJ - from file and using external source

#
# import numpy as np
# np.random.rand()

# # home work 5
# - read and write data
# 
# - read data from website for diff stocks
# - write data to database, mysql, develop code in jupyter notebook
# - use diff query for this data
# - count, mean
# 

import pandas as pd

print("imported pandas")
# !pip install pandas

# ! pip install pandas_datareader

import matplotlib.pyplot as plt
import pandas_datareader as web
import pandas_datareader.data as pd_data

# ! pip install yfinance

# Single ticker from external source - start


stk = web.DataReader("HDFC.NS", data_source="yahoo")
print(stk)
print("hdfc.ns imported from yahoo")

stk['Close'].plot()
plt.show()

print("1. hdfc plotted")
# Single ticker from external source - end

# Date range start
from datetime import datetime

start = datetime(2022, 1, 1)
end = datetime(2022, 3, 31)

print("2. TD plotted")
TD_DataFrame = web.DataReader('TD', 'yahoo', start, end)
TD_DataFrame['Close'].plot()
plt.show()

print("exited plotting TD...going into candlestick")
var = TD_DataFrame.columns
print("printing columns"+var)
# Date range end

# Define the ticker list
# import pandas as pd
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
import yfinance as yf
data = yf.download(tickers_list,'2015-1-1')['Adj Close']

# Print first 5 rows of the data
print("3. Head of multiple tickers")
print(data.head())


# conda info --envs
print("4. Candlestick start")
# df=
#!pip install plotly.graph_objects
import plotly.graph_objects as graph_obj

# 5.1 Plotted with source from a csv file
data_csv = pd.read_csv('Data/AAPL.csv')

data_csv.describe()

candle = graph_obj.Figure(data=[graph_obj.Candlestick(x=data_csv['Date'],
                                                      open=data_csv['Close'],
                                                      high=data_csv['High'],
                                                      low=data_csv['High'],
                                                      close=data_csv['Close'])])

candle.show()

data_csv.plot()


data_csv.columns

data_csv['Close'].plot()
data_csv.info()
data_csv.info
data