# from flask import (
#     Flask,
#     render_template,
#     url_for,
#     request,
#     redirect,
#     jsonify,
#     Blueprint,
#     flash
# )

# #Blueprintでcreate_short_urlアプリを生成する
# create_short_url = Blueprint(
#     "create_short_url",
#     __name__,
#     template_folder="templates",
#     static_folder="static"
# )

# # ----------------短縮URLの生成---------------------------------

# #showFormエンドポイントを作成し、create.htmlを返す
# @create_short_url.route('/')
# def showForm():
#     return render_template(
#         'create_short_url/create.html'
#     )#引数にはtenmplatesフォルダからのパスを記載

# #Form内容の取得
# @create_short_url.route('/shorten-url', methods = ["GET","POST"])
# def createShortUrl():
#     if request.method == "POST":
#             #POST送信されたリクエストを取得する
#         originalURL = request.form.get('originalURL')
#         keyword = request.form.get('keyword')

#         #入力チェック
#         is_valid = True

#         if not originalURL:
#             flash("短縮したいURLを入力してください")
#             is_valid = False
        
#         if not is_valid:
#             return redirect(url_for("showForm"))
        
#         #Flashメッセージをflash関数を使って設定
#         #テンプレートでget_flashed_messages関数を使って取得して表示
#         flash("表示された短縮URLをコピーボタンを押してコピーしてアクセスすると、短縮前のURLにリダイレクトします")

#         return jsonify({   # <==変数に代入して加工？？
#             'description': 'Successful operation',
#             'originalURL': originalURL,
#             'keyword': keyword}), 200
    

#APIを定義
# shortenUrl = Blueprint('shorten-url',
#                 __name__,
#                 url_prefix='/shorten-url')

#APIを登録
# app.register_blueprint(shortenUrl.api)

# ---------------------実際にリクエストせずにアプリの動きを確認するためのテスト用関数


# with app.test_request_context():
#     # 第二引数：create.htmlのname
#     # 第三引数：GETパラメータになる
#     print(url_for("takeURL",
#                 name="originalURL"
#                 #, key="value"
#                 ))