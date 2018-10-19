import aiohttp_jinja2
import jinja2

from aiohttp import web

from routers.routers import routes


app = web.Application()
app.add_routes(routes)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app['static_root_url'] = '/static'
app.router.add_static('/static', 'static', name='static')
web.run_app(app)
