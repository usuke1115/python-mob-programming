import sqlite3 #SQLiteを使うための標準ライブラリー
from flask import (Flask, render_template, url_for)
from item import Item
#上記のようにimportの後に()に各モジュール名を入れておくと
#「行」が長くなったとき、カンマで区切れる

# -----------------SQLiteで使用するSQL文-----------------------------

create_table = """
CREATE TABLE items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    itemname TEXT,
    comment TEXT,
    imgurl TEXT
)
""" #ダブルクヴォーテーション×３で囲むのはPythonのヒアドキュメント
#上記の「SQL文」では、「スペース」や「改行」は無視される
#コマンドを終わらせたい「強制改行」にはセミコロン「;」を用いる

drop_table = "DROP TABLE IF EXISTS items"

insert_str = "INSERT INTO items (itemname, comment, imgurl) VALUES(?,?,?)"
#「?」はプレースホルダー
select_all = "SELECT * FROM items"

# 一番idの値が大きいデータを選ぶ文字列
select_newest = "SELECT * FROM items ORDER BY id DESC LIMIT 1"

# ------------------------------------------------------------

# ----------------------------------------------------------

def get_db():
    dbconn = sqlite3.connect('db/catalog.sqlite3') #なければ新規作成される
    return dbconn #接続オブジェクト

#SQLiteでは、このように指定して「ファイル」が存在しない最初のときは新規作成される
#存在する場合は、そこに読み書きを行う

def close_db(dbconn): #接続オブジェクトを終了する関数
    dbconn.close()



dbapp = Flask(__name__)

@dbapp.route("/")
def index():
    return render_template("index.html")

#接続オブジェクト（⇒executeメソッドが使える）の取得
@dbapp.route("/create_db")
def create_db():
    dbconn = get_db()

    dbconn.execute(drop_table) #まずテーブルがあったら削除
    dbconn.execute(create_table)

    #テストデータ挿入の命令
    dbconn.execute(insert_str,
            ('丸底',
            '底も丸い。肉厚。熱に強いが転がりやすい',
            url_for('static', filename='img/round_flask.jpg') #３つのデータからなるタプル
            )
    )

    #「テーブル」へのデータの挿入は、「SQL」で「COMMIT」の命令を送ってはじめて確定するメソッド
    dbconn.commit()

    #カーソルオブジェクトの取得
    #（挿入したデータを読み出すメソッド）
    cur = dbconn.cursor()

    #select_allは、itemsテーブルから全てのレコードを取り出すSQL文
    #「executeメソッド」の戻り値からさらに「fetchoneメソッド」で「ランダムでどれか１つ」をタプルとして得る
    testdata = cur.execute(select_all).fetchone()

    #DB接続を終了
    close_db(dbconn)

    #タプルをテンプレートに渡す
    return render_template("/db_created.html",testdata=testdata)






