import os

from flask import (Flask, render_template, url_for, request, redirect)

app = Flask(__name__)
def create_app()->Flask:
    """flaskアプリを初期化する関数

    :return: Flaskのオブジェクト
    :rtype: Flask
    """

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


# ----------------短縮URLの生成---------------------------------
@app.route('/form')
def show():
    return render_template(
        'form.html'
    )

@app.route('/shorten-url')
def createShortenUrl():
    pass
