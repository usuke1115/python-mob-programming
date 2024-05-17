from flask import Response, Blueprint


# Blueprintのオブジェクトを生成する
app = Blueprint("health", __name__)


@app.route("/health")
@app.route("/healthcheck")
def health() -> Response:
    return "OK"
