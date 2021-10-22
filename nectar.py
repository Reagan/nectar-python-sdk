from factory.user_factory import UserFactory
from factory.token_factory import TokenFactory
from factory.configurations_factory import ConfigurationsFactory
from factory.credentials_factory import CredentialsFactory
from factory.public_keys_factory import PublicKeysFactory


class Nectar:

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret

    def get_user_factory(self) -> UserFactory:
        return UserFactory(self.key, self.secret)

    def get_token_factory(self) -> TokenFactory:
        return TokenFactory(self.key, self.secret)

    def get_configurations_factory(self) -> ConfigurationsFactory:
        return ConfigurationsFactory(self.key, self.secret)

    def get_credentials_factory(self) -> CredentialsFactory:
        return CredentialsFactory(self.key, self.secret)

    def get_public_keys_factory(self) -> PublicKeysFactory:
        return PublicKeysFactory(self.key, self.secret)



