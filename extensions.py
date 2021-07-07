import json
import requests
from collections import defaultdict

from config import exchanger
class ConverterException(Exception):
    pass
class UserInfo:
    def __init__(self):
        self.f = 'RUB'
        self.t = 'USD'
class UserDB:
    def __init__(self):
        self.db = defaultdict(UserInfo)

    def change_from(self, user_id, val):
        self.db[user_id].f = val
    def change_to(self, user_id, val):
        self.db[user_id].t = val
    def get_pair(self, user_id):
        user= self.db[user_id]
        return user.f, user.t
class Convertor:
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise ConverterException(f'Невозможно перевести одинаковые валюты {base}')

            quote_formatted = quote
            base_formatted = base

        try:
            amount = float(amount)
        except ValueError:
            raise ConverterException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_formatted}&tsyms={base_formatted}')
        result = float(json.loads(r.content)['rates'][base_formatted])*amount
        return round(result, 3)
