#!/usr/bin/env python
# coding: utf-8
import pandas as pd

#import dataset from CSV into Pandas DataFrame
df = pd.read_csv('10Y2Y_SPY.CSV', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df.index, unit='s')

#seperate March data into new DataFrame and isolate March High
march = df['2020-03']
march_high = march.close.idxmax()

#create seperate DataFrames for each dataset
#this step is optional. Used to improve readability
bonds = march[march_high:].close.pct_change()
spy = march[march_high:].SPY.pct_change()

#using the Panda's shift function
print(df.SPY.head())
print(df.SPY.shift().head())
print(df.SPY.shift(-1).head())

#correlation coefficient between bonds and SPY with various shifts
print(bonds.corr(spy))
print(bonds.corr(spy.shift()))
print(bonds.corr(spy.shift(-2)))