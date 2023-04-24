from aiohttp import web_response
from models.auth import _register, _login
import json

async def register(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    data = await _register(username, password)
    return web_response.json_response(json.dumps(data))

async def login(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    data = await _login(username, password)
    return web_response.json_response(json.dumps(data))