import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def hello_world():
    users = User.query.all()
    user_names = ', '.join([user.name for user in users])
    return 'Hello, Docker! Here are the users: ' + user_names

@app.route('/initdb')
def init_db():
    # データベースファイルとディレクトリの存在を確認
    db_path = '/app/data/test.db'
    db_dir = os.path.dirname(db_path)
    
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # データベースのテーブルを作成
    db.create_all()
    # テストユーザーの追加
    if not User.query.first():
        db.session.add(User(name="Alice"))
        db.session.add(User(name="Bob"))
        db.session.add(User(name="Charlie"))
        db.session.commit()
    return "Database initialized."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
