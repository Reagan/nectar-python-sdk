from models.user import User
from factory.user_factory import UserFactory


class Nectar:

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret

    def get_user(self) -> User:
        return UserFactory(self.key, self.secret).get_user()

    def create_user(self, first_name: str, last_name: str, username: str,
                    password: str, phone_no: str, email: str, image_url: str,
                    activated: bool) -> str:
        return UserFactory(self.key, self.secret) \
                .create_user(first_name, last_name, username,
                             password, phone_no, email,
                             image_url, activated)
