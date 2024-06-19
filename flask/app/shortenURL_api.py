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
from app.models import db, Url

import random,string

#ランダム文字列を設定する関数
def random_nstrings(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

#入力されたパスワードをハッシュ化する
import hashlib
sha256 = hashlib.sha256()

shortenURL = Blueprint("shortenURL", __name__)

#短縮URLの生成
@shortenURL.route('/shorten-url', methods = ["GET","POST"])
def create_short_url():
    #if request.method == "POST":
            #POST送信されたリクエストを取得する（↑後でコメントアウトをとればよい？）
        original_url = request.get_json()["original_url"]
        #上の右辺は、request.form.get('original_url')に差し替える？
        keyword = request.get_json()["keyword"]
        #上の右辺は、request.form.get('keyword')に差し替える？

        prefix = "https://"
        hashed_original_url = sha256.update(original_url.encode())
        hashed_original_url = sha256.hexdigest()
        shortened_url = prefix + hashed_original_url[0:5] + keyword
        if len(hashed_original_url[0:5] + keyword) < 15:
            difference = 15 - len(hashed_original_url[0:5] + keyword)
            shortened_url = prefix + hashed_original_url[0:5] + (difference) + keyword

        data = {"original_url": original_url, "shortened_url": shortened_url}
        url_data = jsonify(data)

        #登録するレコードに相当するインスタンスを作る
        latest_shortened_url = Url(
            original_url = data["original_url"],
            shortened_url = data["shortened_url"]
        )

        #上のレコードに相当するインスタンスを追加
        db.session.add(latest_shortened_url)

        #レコード追加をDBに反映
        db.session.commit()

        return url_data










