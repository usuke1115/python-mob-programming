from flask import Blueprint, Response

from app.repositories import UserRepository

# Blueprintのオブジェクトを生成する
app = Blueprint("hello_world", __name__)


@app.route("/")
def hello_world() -> Response:
    user_repository = UserRepository()
    users = user_repository.find_all()
    user_names = ", ".join([user.name for user in users])
    return "Hello, Docker! Here are the users: " + user_names
