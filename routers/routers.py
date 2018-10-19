import aiohttp_jinja2
import requests

from aiohttp.web import json_response
from aiohttp import web


routes = web.RouteTableDef()


@routes.view("/")
class View(web.View):
    @aiohttp_jinja2.template('home/index.html')
    async def get(self):
        return {'s': 'sa'}

    @aiohttp_jinja2.template('home/index.html')
    async def post(self):
        location = (await self.request.post()).get('location')
        print(location)
        if not location:
            return json_response({'error': 'Wrong location'})

        location = location.lower()
        token = "88be56067214c953b2e277c0948327d1"
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': location, 'units': 'metric', 'lang': 'ru', 'appid': token}).json()
        if res['cod'] != 200:
            return json_response({'error': 'Wrong location'})
        res = res['main']
        return json_response({'answer': {
            'temp': res['temp'], 'humidity': res['humidity'], 'pressure': res['pressure']
        }})
