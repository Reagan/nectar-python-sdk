from factory.base import Base


class Credentials(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.credentials_path = "/v1/credentials"

    def get_credentials(self, ref: str):
        return self.get(self.credentials_path, 'ref={}'.format(ref), self.content_type)

    def activate_credentials(self, ref: str):
        endpoint = '{}?ref={}'.format(self.credentials_path, ref)
        return self.put(endpoint, None, self.content_type)

    def deactivate_credentials(self, ref: str):
        endpoint = '{}?ref={}'.format(self.credentials_path, ref)
        return self.delete(endpoint, None, self.content_type)
