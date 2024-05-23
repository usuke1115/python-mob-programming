class BaseConfig:
    """コンフィグの基底クラス"""

    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """開発時に使用するコンフィグクラス"""

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////web/data/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    """テスト時に使用予定のコンフィグクラス"""

    DEBUG = False
    TESTING = True
    DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
