from backend.db.db import weather as weather_model, location as location_model
from backend.create_db import create_db


class Db:
    def __init__(self, config):
        self.engine = create_db(config['postgres'])
        self.config = config

    async def insert_to_location(self, location):
        async with self.engine as engine:
            async with engine.acquire() as conn:
                await conn.execute(location_model.insert().values(location_name=location))
                self.engine = create_db(self.config['postgres'])

    async def insert_to_weather(self, **kwargs):
        async with self.engine as engine:
            async with engine.acquire() as conn:
                await conn.execute(weather_model.insert().values(**kwargs))
                self.engine = create_db(self.config['postgres'])

    async def get_last_location(self, location):
        async with self.engine as engine:
            async with engine.acquire() as conn:
                last = list(await conn.execute(location_model.select()
                                               .where(location_model.c.location_name == location)))[-1]
                self.engine = create_db(self.config['postgres'])
                return last
