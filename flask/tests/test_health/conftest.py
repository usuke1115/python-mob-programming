import pytest
from app import create_app, health

from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture()
def app()-> Flask:
    """アプリケーションの作成"""
    app = create_app()

    app.register_blueprint(health.app)

    return app


@pytest.fixture()
def client(app: Flask)-> FlaskClient:
    """テストクライアントの作成"""
    return app.test_client()
