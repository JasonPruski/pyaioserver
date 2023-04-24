from controllers.auth import login, register

def setup_routes(app):
    app.router.add_post('/auth/login', login)
    app.router.add_post('/auth/register', register)

    app.router.add_static('/', 'static') # must be last!!!