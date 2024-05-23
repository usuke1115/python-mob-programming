from flask import Blueprint, Response

# Blueprintのオブジェクトを生成する
app = Blueprint("health", __name__)


@app.route("/health")
@app.route("/healthcheck")
def health() -> Response:
    """ヘルスチェック用関数

    :return: レスポンス
    :rtype: Response
    """
    return Response(response="OK", status=200)
