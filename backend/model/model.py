import requests


class Weather:
    def __init__(self, config):
        self.url = config['weather']['url']
        self.token = config['weather']['token']

    def get_weather(self, location):
        return requests.get(self.url, params={'q': location, 'units': 'metric', 'appid': self.token}).json()
