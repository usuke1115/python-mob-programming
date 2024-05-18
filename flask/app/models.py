from flask_sqlalchemy import SQLAlchemy


# SQLAlchemyだけの初期化成
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
