import sqlite3 #SQLiteを使うための標準ライブラリー
from flask import (Flask, render_template, url_for, request)
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

# 一番idの値が大きいデータ（一番新しいデータ）を選ぶ文字列
#すでに他のデータが挿入済みの中で、挿入したばかりのデータだけを読み出す
#「全データをidをキーにして降順に並べて、最初の1つを取る」
select_newest = " SELECT * FROM items ORDER BY id DESC LIMIT 1"

select_by_id = " SELECT * FROM items WHERE id = ?"

# ------------------------------------------------------------

dbapp = Flask(__name__)

# ----------------------------------------------------------

def get_db():
    dbconn = sqlite3.connect('db/catalog.sqlite3') #なければ新規作成される
    return dbconn #接続オブジェクト

#SQLiteでは、このように指定して「ファイル」が存在しない最初のときは新規作成される
#存在する場合は、そこに読み書きを行う

def close_db(dbconn): #接続オブジェクトを終了する関数
    dbconn.close()

def insert_dbitem(itemname, comment, imgurl):
    #データベース接続
    dbconn = get_db()

    #引数をテーブルに挿入
    dbconn.execute(insert_str,(itemname, comment, imgurl))
    dbconn.commit()

    #今挿入した値を読み込み直す
    cur = dbconn.cursor()
    new_db_item = cur.execute(select_newest).fetchone()

    #接続終了
    close_db(dbconn)

    #読み込み直したタプルを戻す
    return new_db_item

def create_item_from_dbitem(dbitem):
    return Item(dbitem[0], dbitem[1], dbitem[2], dbitem[3])

def create_item_list():
    #データベースに接続してテーブルの値をすべて読み込む
    dbconn = get_db()
    cur = dbconn.cursor()
    all_db_items = cur.execute(select_all).fetchall()

    #変数all_db_itemsに渡したのでデータベースは終了してよい
    close_db(dbconn)
    
    #Itemオブジェクトのリストを作成
    all_items = []
    for dbitem in all_db_items:
        all_items.append(
            create_item_from_dbitem(dbitem)
        )
    
    return all_items

def create_an_item(id):
    dbconn = get_db()
    cur = dbconn.cursor()
    dbitem = cur.execute(select_by_id, id).fetchone()
    close_db(dbconn)

    return create_item_from_dbitem(dbitem)

# ---------------------------------------------------------------------------------------

@dbapp.route("/")
def index():
    return render_template("index.html")

#接続オブジェクト（⇒executeメソッドが使える）の取得
@dbapp.route("/create_db")
#データベースの初期化
def create_db():
    dbconn = get_db()

    dbconn.execute(drop_table) #まずテーブルがあったら削除
    dbconn.execute(create_table)

    #テストデータ挿入の命令
    dbconn.execute(insert_str,
            ('丸底',
            '底も丸い。肉厚。熱に強いが転がりやすい',
            url_for('static', filename='img/round_flask.jpg')
            #３つのデータからなるタプル
            )
    )

    #「テーブル」へのデータの挿入は、
    #「SQL」で「COMMIT」の命令を送ってはじめて確定するメソッド
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

# ---------------------------------------------------------------------------------------------

@dbapp.route("/insert_item", methods=['GET', 'POST'])
def insert_item():
    if request.method == 'POST':
        file = request.files['photo']
        fname = file.filename
        file.save(f"static/img/{fname}")

        #保存したファイルのURLを取得
        file_url = url_for('static', filename = f"img/{fname}")

        new_dbitem = insert_dbitem(
            request.form['itemname'], request.form['comment'],
            file_url
        )

        #テーブルから読み込み直したタプルからItemオブジェクトを新規作成
        newitem = create_item_from_dbitem(new_dbitem)

        # Itemオブジェクトを引数に渡す。引数名はitem
        return render_template("data_inserted.html", item=newitem)
    
    #GET命令時
    return render_template("insert_item.html")

# -------------------------------------------------------------------------------------------------------------

@dbapp.route("/show_list")
def show_list():

    return render_template("show_list.html", items = create_item_list())

@dbapp.route("/show_item/<id>")
def show_item(id):
    return render_template("show_item.html", item = create_an_item(id))


