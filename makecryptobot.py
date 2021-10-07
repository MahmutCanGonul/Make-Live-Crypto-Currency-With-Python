#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
trades = ['BTCUSDT','FTTUSDT','ADAUSDT']
takeTrade = []
api_key = 'Binance_APIKEY'
secret_key = 'Binance_SECRETKEY'
client = Client(api_key,secret_key)
bsm = BinanceSocketManager(client)


isSame=False

def createframe(msg,i):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns = ['Symbol','Time','Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time,unit='ms')
    if len(takeTrade) > 0:
        if(takeTrade[i-1] == df.iloc[0]['Price']):
            isSame = True
        else:
            isSame = False
    takeTrade.append(df.iloc[0]['Price'])
    return df

engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')
socket = bsm.trade_socket(trades[0])
i=-1
while True: 
    i+=1
    await socket.__aenter__()
    msg = await socket.recv()
    frame = createframe(msg,i)
    frame.to_sql(trades[0],engine,if_exists='append',index=False)
    if isSame == False:
         print(i,frame)
    if i == 100:
        for m in range(len(takeTrade)):
            plt.plot(takeTrade[i])
        plt.show()
        return False
    
    
 





# In[ ]:




