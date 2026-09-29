from bs4 import BeautifulSoup
import requests


def scrape_stock_data(symbol, exchange):
    if exchange == 'NASDAQ':
        url = f"https://finance.yahoo.com/quote/{symbol}"
    elif exchange == 'NSE':
        symbol = symbol+'.NS'
        url = f'http://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " "AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/142.0.0.0 Safari/537.36"}
    
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    current_price = soup.find( "fin-streamer", {"data-field": "regularMarketPrice"} )
    current_price = current_price.get("data-value")
    previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'}).text

    stock_response = {
        'current_price': current_price,
        'previous_close': previous_close,
    }
    
return stock_response

