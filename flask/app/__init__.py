r""""flask shortened URL generation app.

このアプリは短縮URLを作成します。
"""

from app import health, hello_world
from app.app_factory import create_app
from flask import Flask

app: Flask = create_app()

app.register_blueprint(health.app)
app.register_blueprint(hello_world.app)
