from app.models import User, db


class UserRepository:
    """ユーザーモデル操作用リポジトリ"""

    def __init__(self, model: User=User)-> None:
        """コンストラクタ

        :param model: Userモデル, defaults to User
        :type model: User, optional
        """
        self.model = model

    def find_all(self) -> list[User]:
        """全件取得

        :return: Userの全レコード情報
        :rtype: list[User]
        """
        return db.session.execute(db.select(User)).scalars().all()
