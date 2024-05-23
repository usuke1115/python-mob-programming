from app.repositories import UserRepository
from flask import Blueprint, Response

# Blueprintのオブジェクトを生成する
app = Blueprint("hello_world", __name__)


@app.route("/")
def hello_world() -> Response:
    """flaskのサンプル関数

    :return: レスポンス
    :rtype: Response
    """
    user_repository = UserRepository()
    users = user_repository.find_all()
    user_names = ", ".join([user.name for user in users])
    return Response(response="Hello, Docker! Here are the users: " + user_names, status=200)
