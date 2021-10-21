from factory.user_factory import UserFactory


class Nectar:

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret

    def get_user_factory(self) -> UserFactory:
        return UserFactory(self.key, self.secret)





