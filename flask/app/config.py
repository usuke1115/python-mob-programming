from pathlib import Path

class BaseConfig:
    """コンフィグの基底クラス"""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """開発時に使用するコンフィグクラス"""
    DEBUG = True
    TESTING = True
    # SECRET_KEY = "Tjc35z5Xam2VTxMQYrdB"
    # SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    SQLALCHEMY_DATABASE_URI = "sqlite:////web/data/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLをコンソールログに出力する設定
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    """テスト時に使用予定のコンフィグクラス"""
    DEBUG = False
    TESTING = True
    # DATABASE_URI = f"sqlite:///{Path(__file__).parent.parent / 'test.sqlite'}"
    DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLをコンソールログに出力する設定
    SQLALCHEMY_ECHO = True