from aiohttp.web import middleware
from routers.routers import logger


@middleware
async def middleware(request, handler):
    resp = await handler(request)
    if resp.status >= 400:
        logger.error(f"{request.method}-{request.url}-{resp.status}")
        return resp

    logger.info(f"{request.method}-{request.url}-{resp.status}")
    return resp
