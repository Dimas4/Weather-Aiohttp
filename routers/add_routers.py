from routers.routers import routes


def add_routers(app):
    app.add_routes(routes)
