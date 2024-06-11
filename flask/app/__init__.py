r""""flask shortened URL generation app.

このアプリは短縮URLを作成します。
"""

from app import health, hello_world
from app.app_factory import create_app
from flask import Flask

app: Flask = create_app()

#create_short_urlパッケージ（ディレクトリ）からviewsをcreate_short_url_viewsという名前でimportする
from app.create_short_url import views as create_short_url_views

app.register_blueprint(health.app)
app.register_blueprint(hello_world.app)

#register_bluepointを使いviewsのcreate_short_urlをアプリへ登録する
app.register_blueprint(create_short_url_views.create_short_url, url_prefix="/create_short_url")