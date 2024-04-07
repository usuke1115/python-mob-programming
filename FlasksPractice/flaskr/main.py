from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

#今回の場合、flask --app main runで開発用サーバーを起動

@app.route('/')
# デコレータによるルート設定はflask独自の機能ぽい
def index():
    # books = [
    # {
    #     'title': 'はらぺこあおむし',
    #     'price': 1200,
    #     'arrival_day': '2020年7月12日'
    # },
    # {
    #     'title': 'ぐりとぐら',
    #     'price': 990,
    #     'arrival_day': '2020年7月13日'
    # }
    # ]
    #リストは[]、辞書は{key:value}

    con = sqlite3.connect(DATABASE)
    # executeはSQLの文字列を引数とするメソッドと思われる
    db_books = con.execute('SELECT * FROM books').fetchall()
    #executeで取得したデータをfetchallでリスト形式（要素がタプルの２次元配列）にしてまとめる
    # [(１列目のデータ,２列目のデータ,３列目のデータ),(１列目のデータ,２列目のデータ,３列目のデータ),…]

    # データベース接続終了

    books = []
    for row in db_books:
        #booksに要素を入れていく
        books.append({'title': row[0], 'price': row[1], 'arrival_day': row[2], })

    return render_template(
        'index.html',
        books = books
        #上記の変数はこのように引き渡せる。
        #左辺の引数名は何でもよい。（book1とは限らない）
        #引数はいくつでも渡すことができる。
        )
#render_templateでbladeのようにレンダリングするhtmlを指定

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

# SQLiteは表形式のデータを貯めておけるDB
# コンパクトで１ファイルでデータ保存

#登録ボタンが押されたときに実行される関数
#methodsではなくmethodだとエラーになる
@app.route('/register',methods = ['POST'])
#POSTリクエストの場合に下の関数が呼び出される
def register():
    #requestオブジェクトには、input属性に入力して送信された値が入っている
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    #まだinsertしないと、データベースには登録されているわけではない
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?, ?, ?)',
                [title,price,arrival_day])
    #第二引数を上のように記述することでリストの順にデータベースに値が代入されることになる
    con.commit()
    #データベース接続を閉じることで登録が終了する
    con.close()

    #関数indexを呼び出す
    return redirect(url_for('index'))
