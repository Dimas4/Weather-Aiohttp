import aiohttp_jinja2

from exceptions.service.exceptions import WrongLocationError
from exceptions.model.exceptions import ModelRequestError
from logger.create_logger import create_logger
from config.get_config import get_config
from aiohttp.web import json_response
from service.service import Service
from logger.logging import Loader
from aiohttp import web


config = get_config(Loader)
routes = web.RouteTableDef()
service = Service(config)
logger = create_logger(config)


@routes.view("/")
class View(web.View):
    @aiohttp_jinja2.template('home/index.html')
    async def get(self):
        return {'': ''}

    @aiohttp_jinja2.template('home/index.html')
    async def post(self):
        location = (await self.request.post()).get('location')
        try:
            temp, humidity, pressure = await service.validate_query(location)
        except (WrongLocationError, ModelRequestError):
            return json_response({'error': 'Wrong Location'})

        return json_response({'answer': {
            'temp': temp, 'humidity': humidity, 'pressure': pressure
        }})
