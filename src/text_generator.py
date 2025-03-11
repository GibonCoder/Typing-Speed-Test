import requests as req


class TextGenerator:
    def __init__(self):
        self.quotes = {}

    def fetch_text(self):
        res = req.get('https://dummyjson.com/quotes/?limit=10')
        self.quotes = res.json()



