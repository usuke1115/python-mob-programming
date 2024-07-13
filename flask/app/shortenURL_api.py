import random
import string

from app.repositories import UrlRepository

# db（SQLAlchemyインスタンス）とUrlクラスをimportする
from app.schemas import CreateUrlModel, ShortenUrlRequestModel, UrlResponseModel
from flask import Blueprint, Response, current_app, jsonify, request


#ランダム文字列を設定する関数
def random_nstrings(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return "".join(randlst)

#入力されたパスワードをハッシュ化する
import hashlib

sha256 = hashlib.sha256()

# BlueprintでshortenURLアプリを生成する
shortenURL = Blueprint("shortenURL", __name__)

#短縮URLの生成
@shortenURL.route("/shorten-url", methods = ["GET","POST"])
def create_short_url()-> Response:
    request_params = ShortenUrlRequestModel(**request.get_json())

    keyword = request_params.keyword or ""

    prefix = "https://"
    sha256.update(str(request_params.original_url).encode())
    hashed_original_url = sha256.hexdigest()
    shortened_url = prefix + hashed_original_url[0:5] + keyword
    if len(hashed_original_url[0:5] + keyword) < 15:
        difference = 15 - len(hashed_original_url[0:5] + keyword)
        shortened_url = prefix + current_app.config.get("SERVER_NAME") + "/" + hashed_original_url[0:5] + random_nstrings(difference) + keyword


    url_repository = UrlRepository()

    #登録するレコードに相当するインスタンスを作る
    latest_shortened_url = CreateUrlModel(
        original_url = str(request_params.original_url),
        shortened_url = shortened_url,
    )
    #上のレコードに相当するインスタンスを追加
    inserted_id = url_repository.create(latest_shortened_url)

    url_data = url_repository.find_by_id(inserted_id)
    response_model = UrlResponseModel.model_validate(url_data)

    return jsonify(response_model.model_dump()), 201










