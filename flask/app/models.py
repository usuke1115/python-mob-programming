from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(DeclarativeBase, MappedAsDataclass):
    """Base Model Class"""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(insert_default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(insert_default=datetime.now, onupdate=datetime.now)


# SQLAlchemyだけの初期化
db = SQLAlchemy(model_class=Base)

#db.Modelを継承したUserクラスを作る
class User(db.Model):  # type: ignore[name-defined, misc]
    """ユーザーモデル"""

    name: Mapped[str] = mapped_column(nullable=False)

#db.Modelを継承したUserクラスを作る
class Url(db.Model):
    # テーブル名を指定する
    __tablename__ = "urls"
    #カラムを定義する
    original_url: Mapped[str]
    shortened_url: Mapped[str] = mapped_column(unique=True)
