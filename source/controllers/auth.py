from aiohttp import web_response
from aiohttp_session import get_session, new_session
from models.auth import _register, _login
# https://docs.aiohttp.org/en/stable/web_reference.html#aiohttp.web.StreamResponse
# We are encourage using of cookies and set_cookie(), del_cookie() for cookie manipulations.
# httponly !!!!!!!!!!!!!!!!!!!!!!!!
# load_session() and save_session()

async def authenticated(request):
    session = await get_session(request)
    # this is f---ed up and unsafe!!!!!!!!!!!!!!!!!
    # change to jwt? username & password w/ httponly
    if not session[new] and 'uid' in session:
        return web_response.json_response(True)
    else:
        return web_response.json_response(False)

async def register(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    uid = await _register(username, password)
    # this is f---ed up and unsafe!!!!!!!!!!!!!!!!!
    # change to jwt? username & password w/ httponly
    if uid > 0:
        session = await new_session(request)
        session['uid'] = uid
        return web_response.json_response(True)
    else:
        return web_response.json_response(False)

async def login(request):
    data = await request.post()
    username = data['username']
    password = data['password']
    uid = await _login(username, password)
    # this is f---ed up and unsafe!!!!!!!!!!!!!!!!!
    # change to jwt? username & password w/ httponly
    if uid > 0:
        session = await new_session(request)
        session['uid'] = uid
        return web_response.json_response(True)
    else:
        return web_response.json_response(False)

async def logout(request):
    session = await get_session(request)
    session.invalidate()
    return web_response.json_response(True)