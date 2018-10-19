import aiohttp_jinja2

from exceptions.service.exceptions import WrongLocationError
from backend.get_config import get_config
from aiohttp.web import json_response
from service.service import Service
from aiohttp import web


config = get_config()

service = Service(config)
routes = web.RouteTableDef()


@routes.view("/")
class View(web.View):
    @aiohttp_jinja2.template('home/index.html')
    async def get(self):
        return {'': ''}

    @aiohttp_jinja2.template('home/index.html')
    async def post(self):
        location = (await self.request.post()).get('location')
        try:
            response = service.validate_query(location)
        except WrongLocationError:
            return json_response({'error': 'Wrong Location'})

        return json_response({'answer': {
            'temp': response['temp'], 'humidity': response['humidity'], 'pressure': response['pressure']
        }})
