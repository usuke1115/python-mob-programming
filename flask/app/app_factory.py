import os

from flask import Flask


def create_app()->Flask:
    """flaskアプリを初期化する関数

    :return: Flaskのオブジェクト
    :rtype: Flask
    """
    app = Flask(__name__)
    app.config.from_object(os.environ.get("CONFIG_OBJECT"))

    from app.models import db

    db.init_app(app)

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
