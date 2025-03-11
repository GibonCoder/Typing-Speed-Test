import requests as req
import random


class TextGenerator:
    def __init__(self):
        self.quotes = {}
        self.quote = {}

    def fetch_text(self):
        res = req.get('https://dummyjson.com/quotes/?limit=10')
        self.quotes = res.json()['quotes']

    def get_random_quote(self):
        self.quote = random.choice(self.quotes)
