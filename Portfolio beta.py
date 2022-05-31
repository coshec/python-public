import pandas as  pd
from scipy import stats
import yfinance as yf
import numpy as np

_port=[('KPRMILL.NS',200),
('ACC.NS',50),
('NMDC.NS', 800),
('TCS.NS',50),
('GMMPFAUDLR.NS',20),
('ENGINERSIN.NS',1000),
('SHANKARA.NS',60),
('CLNINDIA.NS',330),
('ESCORTS.NS',50),
('OMAXAUTO.NS',800),
('ONGC.NS',1000),
('TITAN.NS',50)]


def get_prices(port:list=None):
    li=[]
    for ticker in port:
        try:
            print(f'Retrieving data for {ticker}:')
            df=yf.Ticker(ticker).history(period='3mo').Close.to_frame()
        except:
            print(f'Data for {ticker} failed')
            continue
        df['ticker']=ticker
        li.append(df)
    #
    df=yf.Ticker('^NSEI').history(period='3mo').Close.to_frame()
    df['ticker']='^NSEI'
    li.append(df)
    #
    dat=pd.concat(li)
    dat.reset_index(inplace=True)
    dat.set_index(['Date','ticker'],inplace=True)
    dat=dat.unstack(level=1)
    dat.columns=[x[1] for x in dat.columns.tolist()]
    #	
    # betas=[]
    # for ticker in port:
    #     (beta,alpha) = stats.linregress(dat['^NSEI'],dat[ticker])[0:2]
    #     betas.append(beta)
    return dat

def get_betas(port):
    dat=get_prices(port.ticker.to_list())
    log_return=np.log(dat/dat.shift(1))
    log_return=log_return.dropna()
#
    betas=[]
    for row in port.iterrows():
        (beta,__)=stats.linregress(log_return['^NSEI'],log_return[row['ticker']])[0:2]
    #    print(f"{ticker} == {beta}")
        betas.append(beta)
    return pd.Series(betas)

def get_last_price(ticker):
    return yf.Ticker(ticker).history(period='1d').Close[0]

def rebalance(port):
    port['change']=0.05 - port.weight
    port['change_qty']=np.round((port.change * port.value.sum()) / port['last_price'],0)
    return

def main():
    port=pd.DataFrame(_port,columns=['ticker','qty'])
    port['beta']=get_betas(port)
    port['last_price']=port.ticker.apply(get_last_price)
    port['value']=np.round(port.qty * port['last_price'],0)
    port['weight']=np.round((port.value / port.value.sum()),3)
    port ['weighted_beta']= np.round(port.beta * port.weight,2)
    #beta weighted NSEI deltas
    nifty_latest=get_last_price('^NSEI')
    port['beta_weighted_nifty_deltas']=np.round(port.qty * port.beta * port['last_price']/nifty_latest,2)
    np.round(port['beta_weighted_nifty_deltas'].sum(),0)
    print(port)


if __name__ == "__main__":
    main()

# (beta,alpha)=stats.linregress(dat['^NSEI'],dat['SHANKARA.NS'])[0:2]


# res=mod.fit()
# print(res.summary())

# =res[0:2]

 