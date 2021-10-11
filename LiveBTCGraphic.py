Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cryptocompare
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation

%matplotlib notebook

plt.style.use('seaborn')

def get_crypto_Price(coin,currency):
    return cryptocompare.get_price(coin,currency)[coin][currency]


def get_crypto_name(coin):
    return cryptocompare.get_coin_list()[coin]['FullName']

price = []
times = []

incordec=0


def animation(i):
    price.append(get_crypto_Price('BTC','USD'))
    times.append(datetime.now())
    if len(price) > 1:
        for i in range(len(price)):
            if price[i] > price[i-1]:
                plt.gcf().canvas.set_window_title("Rising")
            elif price[i] < price[i-1]:
                plt.gcf().canvas.set_window_title("Downing")
          
    plt.cla()
    plt.title(get_crypto_name('BTC')+' Live Graphic')
    plt.xlabel('Date')
    plt.ylabel('USDT $')
    plt.plot_date(times,price,linestyle='solid',ms=0)
    plt.tight_layout()
    
    

ani = FuncAnimation(plt.gcf(),animation,interval=1000)
plt.show()
