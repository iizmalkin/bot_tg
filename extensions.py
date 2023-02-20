import requests
import json
from config import currency_types


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Нельзя перевести {quote} в {base}')

        try:
            quote_ticker = currency_types[quote]
        except KeyError:
            raise APIException(f'Некорректно введена валюта "{quote}"')

        try:
            base_ticker = currency_types[base]
        except KeyError:
            raise APIException(f'Некорректно введена валюта "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Некорректно введено значение {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[currency_types[base]]

        return total_base