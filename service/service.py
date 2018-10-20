from backend.db.db import weather as weather_model, location as location_model
from exceptions.service.exceptions import WrongLocationError
from backend.model.model import Weather
from backend.create_db import create_db


class Service:
    def __init__(self, config):
        self.config = config

        self.weather = Weather(config)
        self.engine = create_db(config['postgres'])

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

        async with self.engine as engine:
            async with engine.acquire() as conn:
                await conn.execute(location_model.insert().values(location_name=location))

                last = list(await conn.execute(location_model.select()
                                               .where(location_model.c.location_name == location)))[-1]
                await conn.execute(weather_model.insert().values(temp=temp, humidity=humidity,
                                                                 pressure=pressure, location_id=last.id))

        self.engine = create_db(self.config['postgres'])

        return temp, humidity, pressure

