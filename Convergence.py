# https://chartink.com/screener/copy-copy-weekly-convergence-5

from operator import index
import kstocks
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas_ta as ta
import pandas as pd

data_dump=kstocks.get_data()
tickers,__=kstocks.get_tickers()


def is_consolidating(df,percentage=0.02):
 df=df[-15:]
 if (df.Close.min()> (df.Close.max() *(1-percentage))):
   return True
   print ('****')
 else:
   return False



def get_convergence(x,tolerance=0.09):
 return_flag=False
 try:
  if (x.ema20 - x.ema50) < x.Close * tolerance:
    if (x.ema50 - x.ema100) < x.Close * tolerance:
      if (x.ema100 - x.ema150) < x.Close * tolerance:
        if (x.ema150 - x.ema200) < x.Close * tolerance:
            if x.Close > x.ema20:
               if (x.ema20-x.ema200) > 0:
                 if x.Close > 50:
                   return_flag=True
                   print(x.Ticker)
 except:
  pass 
 return return_flag

li=[]
for i,ticker in enumerate(tickers):
 df=data_dump[data_dump.Ticker==ticker].copy()
 df['ema20']=ta.ema(df.Close,length=20)
 df['ema50']=ta.ema(df.Close,length=50)
 df['ema100']=ta.ema(df.Close,length=100)
 df['ema150']=ta.ema(df.Close,length=150)
 df['ema200']=ta.ema(df.Close,length=200)
 df['consolidating']=is_consolidating(df)
 li.append(df)
 if i % 20 == 0: print(f'{i}')

ki=pd.concat(li)
ki=ki.loc['2022-01-14']
ki['signal']=ki.apply(lambda x: get_convergence(x,0.02),axis=1)


tick='FOX'
hash=[xx for xx in range(len(li)) if not(li[xx].empty) and li[xx].Ticker[0]==tick]
fig=px.line(li[hash[0]].reset_index(),x='Date',y=['Close','ema50','ema200','ema150','ema20'],title=tick);fig.show()

'''
Adaptation of the 12 exponential moving averages that Australian technical analyst Daryl Guppy uses. 
His GMMA (Guppy multiple moving averages)  plots the following weekly moving averages 
(six short averages 3,5,8,10,12,15 and 6 longer term averages 30,35,40,45,50,60).
'''
li=[]
avgs=[3,5,8,10,12,15,30,35,40,45,50,60]
col_avgs=[''.join(['ema',str(avg)]) for avg in avgs]
shorter_avgs=col_avgs[:6]
longer_avgs=col_avgs[6:]
#shortlist=[]
for i,ticker in enumerate(tickers):
  df=data_dump[data_dump.Ticker==ticker].copy()
  if df.empty:
    continue
  df=df.resample('W').agg({'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum','Ticker':'first'}).copy()
  for c,v in zip(col_avgs,avgs):
      df[c]=ta.ema(df.Close,length=v)
  rec={}
  if df.iloc[-1][shorter_avgs].min() > df.iloc[-1][longer_avgs].max():
      rec['ticker']=ticker
      rec['bullish_trend']=True
      rec['df']=df
  elif df.iloc[-1][shorter_avgs].max() < df.iloc[-1][longer_avgs].min():
      rec['ticker']=ticker
      rec['bullish_trend']=False
      rec['df']=df
  else:
      pass
  if rec: li.append(rec)
  if i%50 == 0: print(f'Processed {i}')

def _plot(df):
  fig2 = make_subplots()
  fig2.add_trace(go.Candlestick(x=df.index,
                                open=df['Open'],
                                high=df['High'],
                                low=df['Low'],
                                close=df['Close'],name='Price'
                              ))
#  fig2.add_trace(go.Scatter(x=df.index,y=df['Close'],name='Price'),secondary_y=False)
  fig2.update_layout(xaxis_rangeslider_visible=False)
  fig2.update_layout(title={'text':df.Ticker[0], 'x':0.5})
  for col in shorter_avgs:
    fig2.add_trace(go.Scatter(x=df.index,y=df[col],marker_color='red',name=col))
  for col in longer_avgs:
    fig2.add_trace(go.Scatter(x=df.index,y=df[col],marker_color='blue',name=col))
  fig2.show()
  return
  
colz=[x for x in df.columns if x.startswith('ema')]
colz.append('Close')

def plot_ticker(li,shortlist):
  ticker_input=input('Enter ticker or press enter:')
  if ticker_input:
    ticker=ticker_input
  else:
    ticker=shortlist[0]
  i=shortlist.index(ticker)
  df=li[i]['df']
  _plot(df)
  return


print('Bullish Tickers\n')
for item in li:
  if item['bullish_trend']:
     print(item['ticker'])


print('\n#_#_#_#_#_#_#_#_#_#_#_#_#_\nBearish Tickers\n')
for item in li:
  if not item['bullish_trend']:
     print(item['ticker'])
  

shortlist=[item['ticker'] for item in li]





