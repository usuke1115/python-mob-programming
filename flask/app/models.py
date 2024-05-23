from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyだけの初期化
db = SQLAlchemy()


class User(db.Model):  # type: ignore[name-defined, misc]
    """ユーザーモデル"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
