from exceptions.service.exceptions import WrongLocationError
from model.model import Weather
from db.model import Db


class Service:
    def __init__(self, config):
        self.config = config
        self.db = Db(config)
        self.weather = Weather(config)

    async def validate_query(self, location):
        if not location:
            raise WrongLocationError

        location = location.lower()
        data = await self.weather.get_weather(location)

        if data['cod'] != 200:
            raise WrongLocationError
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        await self.db.insert_to_location(location)
        last = await self.db.get_last_location(location)
        await self.db.insert_to_weather(temp=temp, humidity=humidity, pressure=pressure, location_id=last.id)

        return temp, humidity, pressure
