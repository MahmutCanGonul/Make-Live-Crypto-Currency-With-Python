import cryptocompare


print("1=> BTCUSD")
print("2=> ETHUSD")
print("3=> ADAUSD")
print("4=> FTTUSD")
print("5=> DOTUSD")
print("6=>SOLUSD")
print("7=>DOGEUSD")

choice = int(input("Enter a number: "))

if choice == 1:
    crypto = "BTC"
    currency = "USD"
elif choice == 2:
    crypto = "ETH"
    currency = "USD"
elif choice == 3:
    crypto = "ADA"
    currency = "USD"
elif choice == 4:
    crypto = "FTT"
    currency = "USD"
elif choice == 5:
    crypto = "DOT"
    currency = "USD"
elif choice == 6:
    crypto = "SOL"
    currency = "USD"
elif choice == 7:
    crypto = "DOGE"
    currency = "USD"
    
print("Checking...")

def get_crypto_Price(coin,currency):
    return cryptocompare.get_price(coin,currency)[coin][currency]


def get_crypto_name(coin):
    return cryptocompare.get_coin_list()[coin]['FullName']

price = []
price_2 = []
times = []
times_2 = []
riskindex = []
incordec=0
count=0
isHugeRisk = False
whenRiskTime=0
whenHugeRiskTime=0

def Table(value):
    price_2.append(get_crypto_Price(crypto,currency))
    if len(price_2) > 1:
        for i in range(len(price_2)):
            if price_2[i] > price_2[i-1]:
                value+=1
            elif price_2[i] < price_2[i-1]:
                value-=1
    if value < -5:
        riskindex.append("Has Risk")
        times_2.append(datetime.now())
        whenRiskTime = len(times_2)
    elif value < -10:
        riskindex.append("Huge Risk")
        times_2.append(datetime.now())
        whenHugeRiskTime = len(times_2)
        isHugeRisk =True
    elif value > 5:
        riskindex.append("Pump")
        times_2.append(datetime.now())
    else:
        times_2.append(datetime.now())
        riskindex.append("Neutral")
           

        
while(count !=500):
    count+=1
    Table(0)

lastprice = price_2[len(price_2)-1]

price_2.sort()
for i in range(len(riskindex)):
    if riskindex[i] == 'Has Risk' and isHugeRisk == False:
        print("There is a risk at ",get_crypto_name(crypto)," Time: ",times_2[whenRiskTime-1]) 
        print("Top Value: ",price_2[len(price_2)-1])
        print("Deep Value: ",price_2[0])
        print("Last Price: ",lastprice)
        if lastprice > price_2[0]:
            print("Last Price is higher than deep price!")
        if lastprice < price_2[0]:
            print("Last Price is lower than deep price")
        if lastprice > price_2[len(price_2)-1]:
            print("Last Price is higher than Top price")
        if lastprice < price_2[len(price_2)-1]:
            print("Last Price is lower than Top price")
            
        return False
    elif riskindex[i] == 'Pump' and isHugeRisk == False:
        print("Pump at ",get_crypto_name(crypto)) 
        print("Top Value: ",price_2[len(price_2)-1])
        print("Deep Value: ",price_2[0])
        print("Last Price: ",lastprice)
        if lastprice > price_2[0]:
            print("Last Price is higher than deep price!")
        if lastprice < price_2[0]:
            print("Last Price is lower than deep price")
        if lastprice > price_2[len(price_2)-1]:
            print("Last Price is higher than Top price")
        if lastprice < price_2[len(price_2)-1]:
            print("Last Price is lower than Top price")
        return True
    elif riskindex[i] == 'Huge Risk' and isHugeRisk == True:
        print("There is a huge risk at ",get_crypto_name(crypto)," Time: ",times_2[whenHugeRiskTime-1]) 
        print("Top Value: ",price_2[len(price_2)-1])
        print("Deep Value: ",price_2[0])
        print("Last Price: ",lastprice)
        if lastprice > price_2[0]:
            print("Last Price is higher than deep price!")
        if lastprice < price_2[0]:
            print("Last Price is lower than deep price")
        if lastprice > price_2[len(price_2)-1]:
            print("Last Price is higher than Top price")
        if lastprice < price_2[len(price_2)-1]:
            print("Last Price is lower than Top price")
            
        return False
        


    
print("There is No risk at ",get_crypto_name(crypto))
print("Top Price: ",price_2[len(price_2)-1])
print("Deep Price: ",price_2[0])
print("Last Price: ",lastprice)

if lastprice > price_2[0]:
        print("Last Price is higher than deep price!")
if lastprice < price_2[0]:
        print("Last Price is lower than deep price")
if lastprice > price_2[len(price_2)-1]:
        print("Last Price is higher than Top price")
if lastprice < price_2[len(price_2)-1]:
        print("Last Price is lower than Top price")

return



