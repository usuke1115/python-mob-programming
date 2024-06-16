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

from app import randomNstrings
#入力されたパスワードをハッシュ化する
import hashlib
sha256 = hashlib.sha256()

shortenURL = Blueprint("shortenURL", __name__)

#Form内容の取得
@shortenURL.route('/shorten-url', methods = ["GET","POST"])
def createShortUrl():
    #if request.method == "POST":
            #POST送信されたリクエストを取得する（↑後でコメントアウトをとればよい？）
        originalURL = input("短縮したいURLをコピペしてください")
        #上の右辺は、request.form.get('originalURL')に差し替える？
        keyword = input("付与するkeywordを入力してください")
        #上の右辺は、request.form.get('keyword')に差し替える？


        #入力チェック
        is_valid = True

        if not originalURL:
            flash("短縮したいURLを入力してください")
            is_valid = False
        
        if not is_valid:
            return render_template('create_short_url/create.html')
        #引数にはtemplatesフォルダからのパスを記載
        
        #flash関数を使ってFlashメッセージを出せるように設定
        #テンプレートでget_flashed_messages関数を使って取得して表示
        flash("表示された短縮URLをコピーボタンを押してコピーしてアクセスすると、短縮前のURLにリダイレクトします")

    #短縮URLの生成
        prefix = "https://"
        hashedOriginalURL = sha256.update(originalURL.encode()).hexdigest()
        shortenedURL = prefix + hashedOriginalURL[0:5] + keyword
        if len(hashedOriginalURL[0:5] + keyword) < 15:
            difference = 15 - len(hashedOriginalURL[0:5] + keyword)
            shortenedURL = prefix + hashedOriginalURL[0:5] + randomNstrings(difference) + keyword

        data = {"originalURL": originalURL, "shortenedURL": shortenedURL}
        URLdata = jsonify(data)
        return URLdata










