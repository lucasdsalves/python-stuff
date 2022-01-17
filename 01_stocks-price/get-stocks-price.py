import requests
import time

ticker = "TGT"

api_key = "YOUR_TWELVE_DATA_API_KEY"

def getStockPrice(tickerSymbol, api):
    url = f"https://api.twelvedata.com/price?symbol={tickerSymbol}&apikey={api}"
    response = requests.get(url).json()

    price = response['price'][:-3]
    return tickerSymbol + ": " + price

stockPrice = getStockPrice(ticker, api_key)   

print(stockPrice)