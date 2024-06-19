r""""flask shortened URL generation app.

このアプリは短縮URLを作成します。
"""

from app import health, hello_world
from app.app_factory import create_app
from flask import Flask
#モデルの宣言
import app.models
from app.db_check import result
from app import shortenURL_api
from app.create_short_url import views

app: Flask = create_app()
app.register_blueprint(health.app)
app.register_blueprint(hello_world.app)

#from画面のviewのレンダリングをアプリへ登録
app.register_blueprint(views.create_short_url, url_prefix="/shorten-url")

#shortenURL_api.pyの短縮URL生成ロジック(shortenURL)をアプリへ登録
app.register_blueprint(shortenURL_api.shortenURL, url_prefix="/api")

app.register_blueprint(result.crud, url_prefix="/sql-result")






