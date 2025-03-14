import requests as req
import random


class TextGenerator:
    def __init__(self):
        self.__quotes = None

    def fetch_text(self):
        res = req.get('https://dummyjson.com/posts/?limit=10')
        self.__quotes = res.json()['posts']

    def get_random_quote(self):
        self.fetch_text()
        return random.choice(self.__quotes)
