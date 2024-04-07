import sqlite3

DATABASE = 'database.db'
#定数としてDATABASEを定義

def create_books_table():
    #接続オブジェクト（データベースへのアクセス）
    con = sqlite3.connect('database.db')
    # con.execute("CREATE TABLE books (title, price, arrival_day)")
    # 上記のようだとbooksというtableがある場合、エラーになるので以下のようにする
    #executeメソッドの引数にはSQL文を文字列として入れる
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)")
    #データベースとの接続を閉じる