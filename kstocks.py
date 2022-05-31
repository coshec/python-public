#D:\d\pyfiles\screener#import pandas_ta
#import pandas_datareader as web
from time import strftime, sleep
from typing_extensions import final 
import pandas as pd
from requests.api import get
import yfinance as yf
#from ta import add_all_ta_features
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands, AverageTrueRange
import numpy as np
from datetime import date 

 

def get_data_yahoo(ticker:str=None,load_type:str=None,start_date:str=None):
   if load_type is not None:
      print(load_type)
      payload=f"period={load_type},interval='1d'"
   sleep(3)
   data = yf.Ticker(ticker).history(period=load_type,interval='1d')
   data['Ticker']=ticker
   data=data.dropna()
   return data

def check_HM(intrvl,data):
 if intrvl == '1mo':
    _period = '3y'
    _resample_freq='M'
 elif intrvl == '1wk':
    _period = '1y'
    _resample_freq='W'
 elif intrvl == '1d':
    _period = '3mo'
    _resample_freq='D'
 else:
    print('Incorrect interval entered. Exiting...')
    return False, None
 weights=np.arange(1,22)
 if _resample_freq!='D':
   data=data.resample(_resample_freq).agg({'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum','Ticker':'first'}).copy()
 else:
    data=data.copy()
 data["rsi_9"] = RSIIndicator(close = data.Close, window = 9).rsi()
 data["wma_21"] = data['rsi_9'].rolling(21).apply(lambda x: np.dot(x,  weights)/weights.sum(), raw=True)
 data["ema_3"]=data["rsi_9"].ewm(span=3).mean()
 if (data.tail(1).rsi_9[0] > 50) & (data.tail(1).wma_21[0] < data.tail(1).ema_3[0]):
    return True, data
 else:
    return False, data

def load_full(tickers):
 master=[]
 for i,ticker in enumerate(tickers):
#  ticker = tickers.loc[i,'Ticker']
   try:
      data=get_data_yahoo(ticker,load_type='3y')
      master.append(data)
   except:
      print ("json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)")
      break
   if i % 5 ==0: print (f"Processed {i}")
 data_dump_incremental=pd.concat(master)
 #DATA_DUMP_FILE=''.join(['D:\\\\d\\pyfiles\\screener\\data_dump-',date.today().strftime("%Y-%b-%d"),'.csv'])
#  DATA_DUMP_FILE=r"D:\d\pyfiles\screener\data_dump-2021-Jul-27.csv"
#  data_dump=pd.read_csv(DATA_DUMP_FILE,index_col=['Date'])
#  data_dump.index=pd.to_datetime(data_dump.index)
#  data_dump=data_dump.append(data_dump_incremental)
 return data_dump_incremental

def load_today(tickers,stock_list):
 start_date=''
 master=[]
 for i,ticker in enumerate(tickers):
#  ticker = tickers.loc[i,'Ticker']
   try:
      data=get_data_yahoo(ticker,load_type='1d')
      master.append(data)
   except:
      print ("json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)")
      break
   if i % 5 ==0: print (f"Processed {i}")
 data_dump_incremental=pd.concat(master)
 print('\nSuccess! Incremental load file created.')
 return data_dump_incremental

def chk_monthly_bb_blast(data_dump,stock_list):
   tickers=list(data_dump.Ticker.unique())
   tickers1=[]
   for i,ticker in enumerate(tickers):
      data=data_dump[data_dump.Ticker==ticker]
      mo,__=check_HM('1mo',data)
   #  data_m['bb_bbh'] = BollingerBands(close=data_m.Close, window=20, window_dev=2).bollinger_hband()
      wk,__=check_HM('1wk',data)
      d,__=check_HM('1d',data)
      if mo and wk and d:
         print(f'Good to go {i}.{ticker}')
         tickers1.append(ticker)
      else:
         pass
   data_m_list=[]
   for ticker in tickers1:
      data=data_dump[data_dump.Ticker==ticker]
      mo,data_m=check_HM('1mo',data)
      data_m['bb_bbh'] = BollingerBands(close=data_m.Close, window=20, window_dev=2).bollinger_hband()
      #  data_m['Ticker']=ticker
      if data_m.tail(1).Close[0] > data_m.tail(1).bb_bbh[0]:
         print(f"Monthly BB blast: {ticker}")
      #    print(data_m.tail(3).to_string())    
         data_m_list.append(data_m)
   final_tickers=pd.concat(data_m_list)
   final_ticker_file=''.join([r'd:\d\pyfiles\screener\final_tickers -',stock_list,'.csv'])
   final_tickers.to_csv(final_ticker_file)
   return final_ticker_file

def _calc_avwap(df_in):
   df=df_in.copy()
   df['avg']=(df.High+df.Low+df.Close)/3
   df['avg_vol']=df.avg * df.Volume
   df['cumsum_price']=df.avg_vol.cumsum()
   df['cumsum_vol']=df.Volume.cumsum()
   df['avwap']= df.cumsum_price / df.cumsum_vol
   return df

def get_avwap(df_in:pd.DataFrame,lowest_point:bool=True):
   '''

   Returns a new dataframe with additional column that includes Anchored VWAP values

   lowest_point: bool
                 Default: True, calculates AVWAP values from lowest point since Jan'20
                 Setting to False calculates AVWAP values from the highest point since Jan'20
   '''
   df=df_in.copy()
   if lowest_point:
      high_low_date = df['2019-12-31':].Low.nsmallest(1).index
   else:
      high_low_date = df['2019-12-31':].High.nlargest(1).index
   one_step_back = df.index.slice_indexer(end=high_low_date.values[0],step=1).stop - 2
   # print(one_step_back)
   # get partial df from anchor date (one_step_back) till latest date
   avwap_df=df.loc[df.iloc[one_step_back:(one_step_back+1)].index.values[0]:]
   # print(avwap_df)
   # pass that partial df for avwap
   avwap_df=_calc_avwap(avwap_df)
   # merge avwap values back into main df
   dff=df.merge(avwap_df['avwap'],left_index=True,right_index=True,how='left')
   return dff


def get_tickers(test_run:bool=False):
 #   final_tickers=chk_monthly_bb_blast()
   if test_run:
      tickers=pd.DataFrame({'Ticker':['AAPL','INTU','CPRT']})
      return tickers,'Test'
   tickers_n100=pd.read_csv(r'D:\d\pyfiles\screener\n100.csv',usecols=['Ticker'])
   tickers_sp500=pd.read_csv(r"D:\d\pyfiles\screener\sp500.csv",usecols=['Ticker'])
   choice={'1':'Nasdaq','2':'S&P500','3':'S&P - Nasdaq','4':'Other'}
   user_input=input(f'\n\n{choice} ::')
   if user_input=='2':
      tickers=tickers_sp500.copy()
   elif user_input == '3':
      tickers=tickers_sp500[~tickers_sp500.Ticker.isin(tickers_n100.Ticker.to_list())].copy()
   elif user_input == '4':
      tickers_dict={'Ticker':[]}
      while True:
         tkr=input('Enter Ticker:')
         if tkr: tickers_dict['Ticker'].append(tkr)
         else: break
      tickers=pd.DataFrame(tickers_dict)
   else:
      tickers=tickers_n100.copy()
   tickers.reset_index(drop=True,inplace=True)
   return list(tickers.Ticker.unique()),choice[user_input]

def get_data():
   from glob import glob
   from os import path
   DATA_DUMP_FILE=glob(f'D:\\d\\pyfiles\\screener\\data_dump-*{date.today().strftime("%Y-%b-%d")}.csv')[0]
   data_dump=pd.read_csv(DATA_DUMP_FILE,index_col=['Date'],parse_dates=['Date'])
   print(f'\n\n Loaded file{DATA_DUMP_FILE.split("\\")[0]}')
   return data_dump

def main():
   tickers,stock_list=get_tickers(test_run=False)
   full_incremental=input('\n\n 1:Full Load, 2:Incremental ::')
   if full_incremental == '1':
      data_dump=load_full(tickers)
      DATA_DUMP_FILE=f'D:\\d\\pyfiles\\screener\\{stock_list}\\data_dump.csv'
      data_dump.to_csv(DATA_DUMP_FILE)
   else:
      data_dump_incremental=load_today(tickers,stock_list)
      DATA_DUMP_FILE_INCREMENTAL=f'D:\\d\\pyfiles\\screener\\delta\\{stock_list}\\data_dump.csv'
      data_dump_incremental.to_csv(DATA_DUMP_FILE_INCREMENTAL)
   #
   final_ticker_file=chk_monthly_bb_blast(data_dump,stock_list)
   final_tickers=pd.read_csv(final_ticker_file,index_col=['Date'])
   final_tickers.index=pd.to_datetime(final_tickers.index)
   #
   final_tickers['MonthlyBB']=np.where(final_tickers.Close>final_tickers.bb_bbh,1,0)
   tickers_MBB=final_tickers['2021-06-01':].groupby('Ticker')['MonthlyBB'].sum().to_frame()
   trade_tickers=list(tickers_MBB[tickers_MBB.MonthlyBB>2].index)
   print("\n\nTickers to trade: ",trade_tickers)
   #data_dump=pd.read_csv(DATA_DUMP_FILE,index_col=['Date'])
   for ticker in trade_tickers:
      data=data_dump[data_dump.Ticker==ticker].copy()
      data['bb_mavg'] = BollingerBands(close=data.Close, window=20, window_dev=2).bollinger_mavg()
      data['bb_mavg5']=data.bb_mavg*1.02
      data['Station']=np.where(data.Close<data.bb_mavg5,'Yes','')
      # if data.tail(1).Station=='Yes':
      print(data.tail(3)) 

if __name__ == "__main__":
    main()
#==


def avwap_scanner(data_dump:pd.DataFrame,tickers:list,lowest_point:bool=True):
   '''
   Scanner for stocks near AVWAP on weekly timeframe
   '''
   for ticker in tickers:
      df_original=data_dump[data_dump.Ticker==ticker]
      __,df_weekly=check_HM('1wk',df_original)
      df=get_avwap(df_weekly,lowest_point=lowest_point)
      df['near_avwap']=np.where(np.logical_and(df.Close<df.avwap*1.03,df.Close>df.avwap*0.97),True,False)
      if df.tail(1).near_avwap[0]:
         print(f'*****\n{df.tail(3)}')
      else:
         #print(df.tail(3))
         pass
   return

def stock_screener(data_dump,timeframe='1wk',atr_multiplier=1,bullish=True,tickers=None):
   '''
   Positional Scanner
   Monthly bullish and near weekly 20 sma
   OR
   Weekly bullish and near daily 20 sma

   same for bearish
   '''
   #
   time_frames=['1mo','1wk','1d']
   higher_time_frame=timeframe
   lower_time_frame=time_frames[time_frames.index(timeframe)+1]
   #
   if tickers == None:
      tickers=list(data_dump.Ticker.unique())
   #
   shortlist={}
   for i,ticker in enumerate(tickers):
      data=data_dump[data_dump.Ticker==ticker]
      __,higher_tf_df=check_HM(higher_time_frame,data)
      if bullish:
         higher_tf_df['BB']=BollingerBands(close=higher_tf_df.Close, window=20, window_dev=2).bollinger_hband()
         higher_tf_df['BB_blast']=np.where(higher_tf_df.Close>higher_tf_df.BB,1,0)
      else:
         higher_tf_df['BB']=BollingerBands(close=higher_tf_df.Close, window=20, window_dev=2).bollinger_lband()
         higher_tf_df['BB_blast']=np.where(higher_tf_df.Close<higher_tf_df.BB,1,0)
      __,lower_tf_df=check_HM(lower_time_frame,data)
      lower_tf_df['sma20']=lower_tf_df.Close.rolling(20).mean()
      try:
            lower_tf_df['ATR']=AverageTrueRange(close=lower_tf_df.Close, high=lower_tf_df.High, \
                              low=lower_tf_df.Low).average_true_range() * atr_multiplier
      except IndexError:
            lower_tf_df['ATR']= 0
      # check if closing is above 20 sma but still near it so check whether it is inside 2 ATR move above 20 sma
      if bullish:
         lower_tf_df['Near_junction']=np.where(np.logical_and(lower_tf_df.Close<(lower_tf_df.ATR + lower_tf_df.sma20), \
                                       lower_tf_df.Close>lower_tf_df.sma20),1,0)
      else:
         lower_tf_df['Near_junction']=np.where(np.logical_and(lower_tf_df.Close>( lower_tf_df.sma20 - lower_tf_df.ATR), \
                                       lower_tf_df.Close<lower_tf_df.sma20),1,0)
      if (higher_tf_df.tail(1).BB_blast[0] == 1) and (lower_tf_df.tail(1).Near_junction[0] == 1):
            print(f'\n\nTicker found {ticker}')
            shortlist[ticker] = 100 * (lower_tf_df.tail(1).Close[0] - lower_tf_df.tail(1).sma20 [0]) / lower_tf_df.tail(1).sma20 [0]
      #monthly_data.append(monthly_data_tkr)
      if i % 20 == 0: print(f'Processed {i} records')
   print(f"{shortlist}")
   return shortlist, higher_tf_df, lower_tf_df




