r""""flask shortened URL generation app.

このアプリは短縮URLを作成します。
"""

from app import health, hello_world
from app.app_factory import create_app
from flask import Flask
import random, string

app: Flask = create_app()

#create_short_urlパッケージ（ディレクトリ）からviewsをcreate_short_url_viewsという名前でimportする
from app.create_short_url import views as create_short_url_views

from app import shortenURL_api as api

app.register_blueprint(health.app)
app.register_blueprint(hello_world.app)

#register_bluepointを使いviewsのcreate_short_urlをアプリへ登録する
#app.register_blueprint(create_short_url_views.create_short_url, url_prefix="/shorten-url")

#15行目でimportしたapi.pyの短縮URL生成ロジック(shorten)をアプリへ登録
app.register_blueprint(api.shortenURL, url_prefix="/api")

#ランダム文字列を設定する関数
def randomNstrings(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)