from factory.base import Base


class ConfigurationsFactory(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.configuration_path = "/v1/configurations"

    def get_configuration(self, ref: str):
        return self.get(self.configuration_path, 'ref={}&detailed=false'.format(ref), self.content_type)

    def activate_configuration(self, ref: str):
        endpoint = '{}?ref={}'.format(self.configuration_path, ref)
        return self.put(endpoint, None, self.content_type)

    def deactivate_configuration(self, ref: str):
        endpoint = '{}?ref={}'.format(self.configuration_path, ref)
        return self.delete(endpoint, None, self.content_type)
