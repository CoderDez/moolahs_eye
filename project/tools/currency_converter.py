import requests 
import os
from decimal import Decimal


def perform_exchange(from_symbol: str, to_symbol: str, amount: float):
    key = os.getenv("EXC_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{key}/pair/{from_symbol}/{to_symbol}"

    conv_rate = Decimal(requests.get(url).json()["conversion_rate"])
    result = (amount * conv_rate).quantize(Decimal("0.01"))
    return result



    




