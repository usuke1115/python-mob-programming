from flask import (
    render_template,
    url_for,
    request,
    redirect,
    jsonify,
    Blueprint,
    flash
)

from flask_sqlalchemy import SQLAlchemy

# db（SQLAlchemyインスタンス）とUrlクラスをimportする
from app.app_factory import db
from app.models import Url

# Blueprintでcrudアプリを生成する
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static"
)


# ----------------短縮したURLの一覧表示---------------------------------

@crud.route('/show_all')
def show_all():
    urls = db.session.query(Url).all()
    return render_template('db_check/index.html',urls=urls)
#引数にはtenmplatesフォルダからのパスを記載

# ---------------最後に短縮したURLの表示---------------------------------
# @crud.route('/show_last')
# def show_last():
#     last_record = db.session.query(Url).order_by(desc(Url.id)).first()
#     return render_template('db_check/index.html',last_record=last_record)

