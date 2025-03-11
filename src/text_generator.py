import requests as req
import random


class TextGenerator:
    def __init__(self):
        self.__quotes = {}
        self.__quote = {}

    def fetch_text(self):
        res = req.get('https://dummyjson.com/quotes/?limit=10')
        self.__quotes = res.json()['quotes']

    def get_random_quote(self):
        self.__quote = random.choice(self.__quotes)
