import numpy as np
import statsmodels.api as sm
from math import *
import pandas as pd
import glob
from functools import reduce
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import statsmodels.tsa.stattools as ts
import yfinance as yf


def corr1(ticker1,ticker2,period:str='1y'):
 if period == '': period = '1y'
 df1=yf.Ticker(ticker1).history(period).Close.to_frame()
 df2=yf.Ticker(ticker2).history(period).Close.to_frame()
 df=df1.merge(df2,left_index=True,right_index=True,how='left')
 df.columns=[ticker1,ticker2]
 return df

def plot_scatter_series(df, ts1, ts2):
    plt.xlabel('%s Price ($)' % ts1)
    plt.ylabel('%s Price ($)' % ts2)
    plt.title('%s and %s Price Scatterplot' % (ts1, ts2))
    plt.scatter(df[ts1], df[ts2])
    plt.show()


def plot_compare(df,ticker1,ticker2):
 months=mdates.MonthLocator()
 fig, ax = plt.subplots()
 ax.plot(df.index, df[ticker1], label=ticker1)
 ax.plot(df.index, df[ticker2], label=ticker2)
 ax.xaxis.set_major_locator(months)
 ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
 #ax.set_xlim(datetime.datetime(2018, 12, 24), datetime.datetime(2020, 12, 23))
 ax.grid(True)
 fig.autofmt_xdate()
 plt.xlabel('Month/Year')
 plt.ylabel('Price (Rs/$)')
 plt.title('%s and %s Daily Prices' % (ticker1,ticker2))
 plt.legend()
 plt.show()
 return
 

def duration(z_array:pd.Series=None):
 z_lag = np.roll(z_array,1)
 z_lag[0] = 0
 z_ret = z_array - z_lag
 z_ret[0] = 0
 #adds intercept terms to X variable for regression
 z_lag2 = sm.add_constant(z_lag)
 model = sm.OLS(z_ret,z_lag2)
 res = model.fit()
 halflife = -log(2) / res.params[1]
 print (f"Average no. of days to reversion: {np.round(halflife,0)}")
 return

ticker1='^NSEI'
ticker2='^NSEBANK'

def main():
    while True:
        ticker1=input('Enter Ticker 1: ')# 'AXISBANK.NS'
        ticker2=input('Enter Ticker 2: ')#'ICICIBANK.NS'
        period=input('Enter period (default=1y): ')
        dx=corr1(ticker1,ticker2,period)
        dx['ratio']= dx[ticker1] / dx[ticker2]
        dx['median']=dx.ratio.describe().to_dict()['mean']
        dx['1sd+']=dx.ratio.describe().to_dict()['mean']+dx.ratio.describe().to_dict()['std']
        dx['1sd-']=dx.ratio.describe().to_dict()['mean']-dx.ratio.describe().to_dict()['std']
        #check for trend, visually and ADF test
        fig,ax=plt.subplots()
        ax.plot(dx.index,dx['ratio'])
        ax.plot(dx.index,dx['median'])
        ax.plot(dx.index,dx['1sd+'])
        ax.plot(dx.index,dx['1sd-'])
        plt.show()
        #plt.plot(dx.ratio);plt.show()
        ts.adfuller(dx.ratio, autolag='AIC')
        # check for regression
        plot_scatter_series(dx['2020-04':],ticker1,ticker2)
        mod = sm.OLS(exog=dx[ticker1], endog=dx[ticker2])
        res=mod.fit()
        print(res.summary())
        #check time for mean reversion
        print("\n\n")
        duration(dx.ratio)
        print("\n\n")
        print(dx.tail(5))
        plot_compare(dx,ticker1,ticker2)
        if input('Enter Y/y to continue: ').upper() != 'Y':
            break
    return


if __name__ == "__main__":
    main()


