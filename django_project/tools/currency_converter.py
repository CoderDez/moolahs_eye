import requests 
import os
from decimal import Decimal


def perform_exchange(from_symbol: str, to_symbol: str, amount: Decimal):
    """
    Performs currency exchange calculation based on provided symbols and amount.

    Args:
    - from_symbol (str): The symbol of the currency to convert from.
    - to_symbol (str): The symbol of the currency to convert to.
    - amount (Decimal): The amount of currency to be converted.

    Returns:
    - Decimal: The converted amount based on the exchange rate.
    """

    try:
        key = os.getenv("EXC_API_KEY")
        url = f"https://v6.exchangerate-api.com/v6/{key}/pair/{from_symbol}/{to_symbol}/"

        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

        conv_rate = Decimal(response.json()["conversion_rate"])
        result = (amount * conv_rate).quantize(Decimal("0.01"))
        return result

    except Exception as e:
        print(f"An error occurred during currency exchange: {e}")
        return Decimal(0)


    




