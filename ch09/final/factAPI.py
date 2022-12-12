import requests


class FactAPI:

    def __init__(self):
        self.url = "https://uselessfacts.jsph.pl/random.json?language=en"

    def get(self):  #returns a random fact
        r = requests.get(self.url)
        response = r.json()
        if response.get('text'):
            return response['text']
        else:
            return None
