from aiohttp import web

from routers.add_routers import add_routers
from backend.create_app import create_app


if __name__ == "__main__":
    # app['config'] =
    app = create_app()

    add_routers(app)
    web.run_app(app)
