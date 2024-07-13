from app.models import Url, User, db
from app.schemas import CreateUrlModel


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


class UrlRepository:
    """URLモデル操作用リポジトリ"""

    def __init__(self, model: Url=Url)-> None:
        """コンストラクタ

        :param model: Urlモデル, defaults to Url
        :type model: Url, optional
        """
        self.model = model

    def find_by_id(self, url_id: int) -> list[Url]:
        """IDをもとにレコードを1件取得

        :param id: 取得対象のID
        :type id: int
        :return: _description_
        :rtype: list[Url]
        """
        return db.session.execute(db.select(Url).where(Url.id == url_id)).scalars().first()

    def create(self, url_data: CreateUrlModel)-> int:
        """レコードの作成

        :param url_data: 登録情報
        :type url_data: Url
        :return: 登録したレコードのID
        :rtype: int
        """
        #上のレコードに相当するインスタンスを追加
        stmt = db.insert(Url).returning(Url.id)
        result = db.session.execute(stmt, url_data.model_dump())
        return result.mappings().first()["id"]
