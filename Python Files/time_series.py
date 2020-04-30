#!/usr/bin/env python
# coding: utf-8
import pandas as pd


TSLA_df = pd.read_csv('TSLA.CSV')

#the following commented method automatically creates a datetime index
#TSLA_df = pd.read_csv('TSLA.CSV', index_col=0, parse_dates=True)
print(TSLA_df)

#manual method of setting index to date
TSLA_df.set_index('date', inplace=True)
print(TSLA_df)

#checking the dtype for the DataFrame index
print(TSLA_df.index[:4])

#converting the DataFrame index to datetime64
TSLA_df.index = pd.to_datetime(TSLA_df.index)
print(TSLA_df.index[:4])