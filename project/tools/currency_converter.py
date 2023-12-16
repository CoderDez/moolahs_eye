from bs4 import BeautifulSoup
import requests 
from decimal import Decimal


def perform_exchange(amount: float, from_symbol: str, to_symbol: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{from_symbol}{to_symbol}=X/'

    source = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(source, 'lxml')

    # if from symbol is USD set to empty string
    # rationale: data-symbol on Yahoo Finance just has 'to_currency'=X
    if from_symbol == "USD":
        from_symbol = ""

    element = soup.find(
        attrs={
            'data-field': 'regularMarketPrice', 
            'data-symbol': f'{from_symbol}{to_symbol}=X'
        }
    )

    value = Decimal(element.get("value")) if element else Decimal('0.0')
    result = (amount * value).quantize(Decimal('0.01'))
    return result

