import base64
from cryptography import fernet
from aiohttp import web
from aiohttp_index import IndexMiddleware
# from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from routes import setup_routes

app = web.Application(
    middlewares=[
        IndexMiddleware(),
        EncryptedCookieStorage(
            base64.urlsafe_b64decode( fernet.Fernet.generate_key() ))])
# setup(
#     app,
#     EncryptedCookieStorage(
#         ))
setup_routes(app)
# ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# ssl_context.load_cert_chain('domain_srv.crt', 'domain_srv.key')
web.run_app(app) #, ssl_context=ssl_context)