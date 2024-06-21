from flask_sqlalchemy import SQLAlchemy

from app.app_factory import db
from datetime import datetime


#db.Modelを継承したUserクラスを作る
class User(db.Model):  # type: ignore[name-defined, misc]
    """ユーザーモデル"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

#db.Modelを継承したUserクラスを作る
class Url(db.Model):
    # テーブル名を指定する
    __tablename__ = "urls"
    #カラムを定義する
    #primary_keyにauto_increamentが組み込まれている。
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String)
    shortened_url = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)