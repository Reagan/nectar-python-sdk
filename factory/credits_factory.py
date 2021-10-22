from factory.base import Base


class CreditsFactory(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.credits_path = "/v1/credits"
        self.transactions_path = "/v1/transactions"

    def get_credits(self):
        return self.get(self.credits_path, '', self.content_type)

    def get_transactions(self):
        return self.get(self.transactions_path, '', self.content_type)
