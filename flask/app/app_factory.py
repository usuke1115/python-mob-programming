import os, logging

from pathlib import Path

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

# SQLAlchemyだけの初期化
db = SQLAlchemy()

def create_app()->Flask:
    """flaskアプリを初期化する関数

    :return: Flaskのオブジェクト
    :rtype: Flask
    """

    app = Flask(__name__)
    app.config.from_object(os.environ.get("CONFIG_OBJECT"))

    #ロガーのログレベルを設定
    app.logger.setLevel(logging.DEBUG)

    #リダイレクトを中断しないようにする
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    # ブラウザの右側にデバッグツールバーが表示されるようにする
    toolbar = DebugToolbarExtension(app)

    # ---------------------------------------------------------------------------------
    from app.models import db

    #SQLAlchemyとアプリを連携する
    db.init_app(app)

    #Migrateとアプリを連携
    Migrate(app,db)

    # 開発時のみ、DBのsqliteにUserデータを作成する
    if app.config.get("DEBUG"):
        # DBの初期化
        with app.app_context():
            db.create_all()
            # テストユーザーの追加
            from app.models import User

            if not User.query.first():
                db.session.add(User(name="Alice"))
                db.session.add(User(name="Bob"))
                db.session.add(User(name="Charlie"))
                db.session.commit()

    return app
