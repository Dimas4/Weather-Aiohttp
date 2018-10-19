from exceptions.service.exceptions import WrongLocationError
from backend.model.model import Weather


class Service:
    def __init__(self, config):
        self.weather = Weather(config)

    def validate_query(self, location):
        if not location:
            raise WrongLocationError

        location = location.lower()
        data = self.weather.get_weather(location)
        if data['cod'] != 200:
            raise WrongLocationError
        return data['main']

