from aiohttp import web_response
from models.user import get_users
import json

async def get_user(request):
    print("index controller called")
    data = await get_users()
    print("data retreived", data)
    return web_response.json_response(json.dumps(data))
