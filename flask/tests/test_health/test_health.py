from flask.testing import FlaskClient


def test_health_request(client: FlaskClient)-> None:
    """ヘルスチェックのチェック"""
    response = client.get("/health")
    assert b"OK" in response.data
    assert response.status_code == 200
