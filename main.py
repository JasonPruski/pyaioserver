from aiohttp import web
from aiohttp_index import IndexMiddleware
from routes import setup_routes

app = web.Application(middlewares=[IndexMiddleware()])
setup_routes(app)
web.run_app(app)
