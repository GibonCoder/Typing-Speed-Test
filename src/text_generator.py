import requests as req
import random


class TextGenerator:
    def __init__(self):
        self.__quotes = None
        self.__quote = None

    def fetch_text(self):
        res = req.get('https://dummyjson.com/quotes/?limit=10')
        self.__quotes = res.json()['quotes']

    def get_random_quote(self):
        return random.choice(self.__quotes)
