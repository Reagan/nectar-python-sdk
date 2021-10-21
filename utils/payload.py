import json


class Payload:

    def __init__(self, params: dict):
        self.params = params

    def to_json(self):
        return json.dumps(self.params)

    def __str__(self):
        return json.dumps(self.params).__str__()
