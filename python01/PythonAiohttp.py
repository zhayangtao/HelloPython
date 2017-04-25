import asyncio
from aiohttp import web
async def index(request):
    await asyncio.sleep(1)
    return web.Response(body=b'<h1>Index</h1>')
async def hello(request):
    pass
