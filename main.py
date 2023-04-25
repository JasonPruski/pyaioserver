import base64
from cryptography import fernet
from aiohttp import web
from aiohttp_index import IndexMiddleware
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from routes import setup_routes

app = web.Application(middlewares=[IndexMiddleware()])
setup(
    app,
    EncryptedCookieStorage(
        base64.urlsafe_b64decode( fernet.Fernet.generate_key() )))
setup_routes(app)
web.run_app(app)