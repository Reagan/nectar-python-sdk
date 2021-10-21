from factory.base import Base


class PublicKeys(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.public_keys_path = "/v1/public_keys"

    def create_public_key(self, name: str,
                          key: str, activated: bool):
        payload = create_payload({
            'name': name,
            'key': key,
            'activated': activated,
        })
        return self.put(self.public_keys_path, payload, self.content_type)

    def activate_public_keys(self, ref: str):
        endpoint = '{}?ref={}'.format(self.credentials_path, ref)
        return self.put(endpoint, None, self.content_type)

    def deactivate_public_keys(self, ref: str):
        endpoint = '{}?ref={}'.format(self.credentials_path, ref)
        return self.delete(endpoint, None, self.content_type)
