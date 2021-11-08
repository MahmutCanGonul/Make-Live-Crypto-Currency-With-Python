from binance.client import Client
import pandas as pd
from tqdm import tqdm

#Request part
client = Client()
info = client.get_exchange_info()



#Get the symbols in info object
symbols = [x['symbol'] for x in info['symbols']]
exclude = ['UP','DOWN','BEAR','BULL']
non_lvl = [symbol for symbol in symbols if all(excludes not in symbol for excludes in exclude)]
#Just get USDT exchange rate
usdt = [symbol for symbol in non_lvl if symbol.endswith("USDT")]
klines = {}

#Get the all crypto's exchange to usdt, last 1 hour 
for symbol in tqdm(usdt):
    klines[symbol] = client.get_historical_klines(symbol,"1m","1 hour UTC")
    
    
#Create empty array returns hold the cumrets data, symbols2 hold the symbols     
returns,symbols2 = [],[]

for symbol in usdt:
    if len(klines[symbol]) > 0:
        cumret = (pd.DataFrame(klines[symbol])[4].astype(float).pct_change()+1).prod()-1
        returns.append(cumret)
        symbols2.append(symbol)
        
        
#Get the all data on returnDF object        
returnDF = pd.DataFrame(returns,index=symbols2,columns=['ret'])
#Return best performing coins TOP-10
returnDF.ret.nlargest(10)  
