from models.user import User
from factory.user_factory import UserFactory


class Nectar:

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret

    def get_user(self) -> User:
        return UserFactory(self.key, self.secret).get_user()

