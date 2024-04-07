#初期化処理を記載
from flask import Flask
app = Flask(__name__)  #flaskのオブジェクトを作成
import flaskr.main

from flaskr import db
#空のテーブルを作る
db.create_books_table()








