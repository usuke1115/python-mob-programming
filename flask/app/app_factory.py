import os

from flask import (Flask, render_template, url_for, request, redirect, jsonify,Blueprint)

app = Flask(__name__)
app.config.from_object(os.environ.get("CONFIG_OBJECT"))

def create_app()->Flask:
    """flaskアプリを初期化する関数

    :return: Flaskのオブジェクト
    :rtype: Flask
    """

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
#endpointをshowFormに指定
@app.route('/')
def show():
    return render_template(
        'form.html'
    )#引数にはtenmplatesフォルダからのパスを記載

#Form内容の取得
@app.route('/takeURL', methods = ["GET","POST"])
def takeURL():
    #POST送信されたリクエストを取得する
    originURL = request.form.get('originalURL')
    keyword = request.form.get('keyword')

    return jsonify({
        'description': 'Successful operation',
        'originalURL': originURL,
        'keyword': keyword}), 200


#APIを定義
# shortenUrl = Blueprint('shorten-url',
#                 __name__,
#                 url_prefix='/shorten-url')

#APIを登録
# app.register_blueprint(shortenUrl.api)

# ---------------------実際にリクエストせずにアプリの動きを確認するためのテスト用関数


with app.test_request_context():
    # 第二引数：form.htmlのname
    # 第三引数：GETパラメータになる
    print(url_for("takeURL",name="originalURL", key="value"))