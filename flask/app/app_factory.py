import os, logging


from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    jsonify,
    Blueprint,
    flash
)

# from flask_debugtoolbar import DebugToolbarExtension

def create_app()->Flask:
    """flaskアプリを初期化する関数

    :return: Flaskのオブジェクト
    :rtype: Flask
    """

    app = Flask(__name__)
    app.config.from_object(os.environ.get("CONFIG_OBJECT"))

    # # セッションが必要<==Flashメッセージを使いたい
    # #SECRET_KEYを追加（<==セッション情報を使えるようにする）
    # secretkey = randomNstrings(20)
    # app.config["SECRET_KEY"] = secretkey

    #ロガーのログレベルを設定
    app.logger.setLevel(logging.DEBUG)

    #リダイレクトを中断しないようにする
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    # #ブラウザの右側にデバッグツールバーが表示されるようにする
    # toolbar = DebugToolbarExtension(app)

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
