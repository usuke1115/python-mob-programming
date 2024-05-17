import sqlite3

DATABASE = 'urls.db'
#定数としてDATABASEを定義

def create_table():
    #接続オブジェクト（データベースへのアクセス）
    con = sqlite3.connect('urls.db')
    # con.execute("CREATE TABLE urls (originurl, newurl)")
    # 上記のようだとurlsというtableがある場合、エラーになるので以下のようにする
    #executeメソッドの引数にはSQL文を文字列として入れる
    con.execute("CREATE TABLE IF NOT EXISTS urls (originurl, newurl)")
    #データベースとの接続を閉じる
    con.close()
    