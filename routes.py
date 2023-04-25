from controllers.auth import authenticated, login, register

def setup_routes(app):
    app.router.add_get('/auth/authenticated', authenticated)
    app.router.add_post('/auth/login', login)
    app.router.add_post('/auth/register', register)

    app.router.add_static('/', 'static') # must be last!!!