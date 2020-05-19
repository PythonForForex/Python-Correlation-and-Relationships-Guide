#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

#grab tickers from csv file
watchlist_df = pd.read_csv('watchlist.csv', header=None)
watchlist = watchlist_df.iloc[0].tolist()

'''instantiate TimeSeries class from alpha_vantage library
**you must have API keys stored as environment variables for this to work
check out the Alpha Vantage guide on the AlgoTrading 101 blog for more details'''
app = TimeSeries(output_format='pandas')

#itter through watchlist and retrieve daily price data
stocks_df = pd.DataFrame()
for ticker in watchlist:
    alphav_df = app.get_daily_adjusted(ticker)
    alphav_df = alphav_df[0]
    alphav_df.columns = [i.split(' ')[1] for i in alphav_df.columns]

    stocks_df[ticker] = alphav_df['adjusted'].pct_change()

#print time-series df
stocks_df = stocks_df[1:11] # Use only the last 10 days for example purposes
print(stocks_df.head())

#print correlation between AAPL and ADBE
print(stocks_df.AAPL.corr(stocks_df.MSFT))
#print correlation between AAPL and NFLX
print(stocks_df.AAPL.corr(stocks_df.NFLX))

#print correlation using kendall method
print(stocks_df.AAPL.corr(stocks_df.NFLX, method='kendall'))
#print correlation using spearman method
print(stocks_df.AAPL.corr(stocks_df.NFLX, method='spearman'))

#correlation matrix
print(stocks_df.corr())

#strongest correlated stock with Netflix
nflx_corr_df = stocks_df.corr().NFLX
print(nflx_corr_df[ nflx_corr_df < 1 ].idxmax())

#Negatively correlated with Netflix
print(nflx_corr_df.idxmin())


#visualizing with the Seaborn library
import seaborn as sns
import matplotlib.pyplot as plt

#default heatmap
ax = sns.heatmap(stocks_df.corr())
plt.show()

#customized colors heatmap
ax = sns.heatmap(stocks_df.corr(), cmap='RdYlGn', linewidths=.1)
plt.show()

#create covariance matrix
stocks_df.cov()