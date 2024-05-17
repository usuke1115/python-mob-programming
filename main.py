from flask import Flask, render_template, request, redirect, url_for
import sqlite3, db, randomstrings

#空のテーブルを作る
db.create_table()

app = Flask(__name__)  #flaskのオブジェクトを作成
DATABASE = 'urls.db'

#今回の場合、flask --app main runで開発用サーバーを起動

# -------------------------------------------------------------------------------------

@app.route('/')
def form():
    return render_template('form.html')

# SQLiteは表形式のデータを貯めておけるDB
# コンパクトで１ファイルでデータ保存

#登録ボタンが押されたときに実行される関数
#methodsではなくmethodだとエラーになる
@app.route('/converting',methods = ['POST'])
#POSTリクエストの場合に下の関数が呼び出される
def convert():
    #requestオブジェクトには、input属性に入力して送信された値が入っている
    originurl = request.form['originurl']
    keyword = request.form['keyword']

    # キーワード + ハイフン + ランダム文字列で組み込むつもりでした！
    # 例
    # 元のURL：https://aaa.com
    # キーワード：book
    # 短縮後のURL：https://○○.○○/book-HyJU

    randomstrings = randomstrings(4)


    #まだinsertしないと、データベースには登録されているわけではない
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO urls VALUES(?, ?)',
                [originurl,newurl])
    #第二引数を上のように記述することでリストの順にデータベースに値が代入されることになる
    con.commit()
    #データベース接続を閉じることで登録が終了する
    con.close()

    #関数indexを呼び出す
    return redirect(url_for('show'))

@app.route('/converted')
def show():
    con = sqlite3.connect(DATABASE)
    # executeはSQLの文字列を引数とするメソッドと思われる
    firsturl = con.execute('SELECT * FROM urls').fetchone()
    #executeで取得したデータをfetchallでリスト形式（要素がタプルの２次元配列）にしてまとめる
    # [(１列目のデータ,２列目のデータ,３列目のデータ),(１列目のデータ,２列目のデータ,３列目のデータ),…]

    # データベース接続終了

    urls = []
    for row in urls:
        #booksに要素を入れていく
        urls.append({'originurl': row[0], 'newurl': row[1]})

    return render_template(
        'form.html',
        urls = urls
        #上記の変数はこのように引き渡せる。
        #左辺の引数名は何でもよい。
        #引数はいくつでも渡すことができる。
        )
#render_templateでbladeのようにレンダリングするhtmlを指定
