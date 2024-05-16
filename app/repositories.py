from app.models import User


class UserRepository:
    def __init__(self, model=User):
        self.model = model

    def find_all(self) -> list[User]:
        return User.query.all()
