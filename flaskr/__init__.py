from flask import Flask

from flaskr.app_factory import create_app
from flaskr import health, hello_world

app: Flask = create_app()

app.register_blueprint(health.app)
app.register_blueprint(hello_world.app)
