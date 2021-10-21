from factory.base import Base


class Configuration(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.configuration_path = "/v1/configurations"

    def get_configuration(self, ref: str, detailed: bool):
        return self.get(self.configuration_path, 'ref={}&detailed={}'.format(ref, detailed), self.content_type)

    def activate_configuration(self, ref: str):
        endpoint = '{}?ref={}'.format(self.configuration_path, ref)
        return self.put(endpoint, None, self.content_type)

    def deactivate_configuration(self, ref: str):
        endpoint = '{}?ref={}'.format(self.configuration_path, ref)
        return self.delete(endpoint, None, self.content_type)
