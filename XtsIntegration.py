from io import StringIO

from Connect import XTSConnect
import pandas as pd
from datetime import datetime

xt =None
xtm=None
def login(API_KEY,API_SECRET,source):
    global xt
    xt = XTSConnect(API_KEY, API_SECRET, source)
    response = xt.interactive_login()
    print("response interactive xts: ",response)

def marketapilogin(API_KEY,API_SECRET,source):
    global xtm
    xtm = XTSConnect(API_KEY, API_SECRET, source)
    response = xtm.marketdata_login()
    print("response market xts: ",response)

def ExchangeSegment():
    exchangesegments=[xtm.EXCHANGE_NSEFO]
    nfores= xtm.get_master(exchangesegments)
    masterdf= pd.read_csv(StringIO(nfores['result']),sep='|',usecols=range(19),header=None,low_memory=False)
    print(masterdf)
    print(masterdf.columns)