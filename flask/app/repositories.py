from app.models import db, User


class UserRepository:
    def __init__(self, model=User):
        self.model = model

    def find_all(self) -> list[User]:
        return db.session.execute(db.select(User.__table__)).mappings()
