infy=pd.read_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\INFY.csv")
tcs=pd.read_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\TCS.csv")
wipro=pd.read_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\WIPRO.csv",usecols=['Date','Average Price'])
techm=pd.read_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\TECHM.csv",usecols=['Date','Average Price'])

bfinsv=pd.read_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\corr3\01-11-2019-TO-30-10-2020BAJAJFINSVALLN.csv",usecols=['Date','Average Price'])
bajfin=pd.read_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\corr3\01-11-2019-TO-30-10-2020BAJFINANCEALLN.csv",usecols=['Date','Average Price'])



infy.set_index(infy.Date,drop=True,inplace=True)
tcs.set_index(tcs.Date,drop=True,inplace=True)
wipro.set_index(wipro.Date,drop=True,inplace=True)
techm.set_index(techm.Date,drop=True,inplace=True)

bfinsv.set_index(bfinsv.Date,drop=True,inplace=True)
bajfin.set_index(bajfin.Date,drop=True,inplace=True)

df=bfinsv.merge(bajfin['Average Price'],left_index=True,right_index=True,how='left')

df=infy.merge(tcs['Average Price'],left_index=True,right_index=True,how='left')
dg=df['Average Price_x','Average Price_y']

dh=dg.merge(wipro['Average Price'],left_index=True,right_index=True,how='left')
dh.rename(columns={'Average Price_x':'INFY','Average Price_y':'TCS','Average Price':'WIPRO'},inplace=True)

di=dh.merge(techm['Average Price'],left_index=True,right_index=True,how='left')

di.rename(columns={'Average Price':'TECHM'},inplace=True)
di.corr()

           INFY       TCS     WIPRO     TECHM
INFY   1.000000  0.752389  0.695674  0.560792
TCS    0.752389  1.000000  0.882938  0.701407
WIPRO  0.695674  0.882938  1.000000  0.741797
TECHM  0.560792  0.701407  0.741797  1.000000

INFY - 1200 * 747 = 896,400 * 36.68% = 328800
TCS - 300 * 2115 = 634,500  * 37.06% = 235146

Ratio = 1.41

di.to_csv(r"G:\Kaushik Kochhar\d\pyfiles\MorningStar\consolidated.csv")
