from flask import Flask

from app.app_factory import create_app
from app import health, hello_world

app: Flask = create_app()

app.register_blueprint(health.app)
app.register_blueprint(hello_world.app)
