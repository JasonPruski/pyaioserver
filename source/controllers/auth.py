import jwt
from email.message import EmailMessage
import asyncio
from aiohttp import web_response
from aiohttp_session import get_session, new_session
import aiosmtplib
from models.auth import _register, _login, _verify
from resources.jwt_key import key

async def authenticated(request):
    session = await get_session(request)
    if 'jwt' in session:
        return web_response.json_response(True)
    else:
        return web_response.json_response(False)

async def get_user_id(request):
    session = await get_session(request)
    if 'jwt' in session:
        credentials = jwt.decode(encoded, key, algorithms=["HS512"])
        return await _login(credentials['username'], credentials['password'])
    else:
        return 0

async def register(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    uid = await _register(username, password)
    if uid > 0:
        session = await new_session(request)
        session['jwt'] = jwt.encode(
            {'username': username, 'password': password}, 
            jwt_key.key, algorithm="HS512")
        # to do: send confirmation email
        message = EmailMessage()
        message["From"] = "jasonmilespruski@outlook.com"
        message["To"] = username
        message["Subject"] = "http://161.35.100.26:8080/auth/"+jwt.encode(
            {'username': username}, 
            key, algorithm="HS512")
        message.set_content(confirmation_email.content)
        await asyncio.get_running_loop().run_in_executor(
            None,
            aiosmtplib.send(message, hostname="127.0.0.1", port=25))
        return web_response.json_response(True)
    else:
        return web_response.json_response(False)

async def login(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    uid = await _login(username, password)
    if uid > 0:
        session = await new_session(request)
        session['jwt'] = jwt.encode(
            {'username': username, 'password': password}, 
            key, algorithm="HS512")
        return web_response.json_response(True)
    else:
        return web_response.json_response(False)

async def logout(request):
    session = await get_session(request)
    session.invalidate()
    return web_response.json_response(True)

async def verify(request):
    await _verify(
        jwt.decode(
            request.match_info['token'],
            key,
            algorithms=["HS256"])['username'])
    return web_response.json_response(True)