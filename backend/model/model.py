import aiohttp


class Weather:
    def __init__(self, config):
        self.url = config['weather']['url']
        self.token = config['weather']['token']

    async def get_weather(self, location):
        async with aiohttp.ClientSession() as session:

            async with session.get(self.url, params={'q': location, 'units': 'metric', 'appid': self.token}) as resp:

                return await resp.json()
