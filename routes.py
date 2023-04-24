from controllers.user import get_user

def setup_routes(app):
    app.router.add_get('/user', get_user)
    app.router.add_static('/', 'static')
