from factory.base import Base
from factory.base import create_payload
from factory.base import validate_response
from factory.base import i
from models.user import User


def create_user_params(first_name: str, last_name: str, username: str,
                       password: str, phone_no: str, email: str, image_url: str,
                       activated: bool) -> dict:
    return {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'password': password,
        'phone_no': phone_no,
        'email': email,
        'image_url': image_url,
        'activated': activated
    }


def create_update_user_params(ref: str, first_name: str, last_name: str, username: str,
                              password: str, phone_no: str, email: str, image_url: str,
                              activated: bool) -> dict:
    update_user_params = {
        'ref': ref
    }
    user_params = create_user_params(first_name, last_name, username, password,
                                     phone_no, email, image_url, activated)
    return {**update_user_params, **user_params}


class UserFactory(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.users_path = "/v1/users"

    def create_user(self, first_name: str, last_name: str, username: str,
                    password: str, phone_no: str, email: str, image_url: str,
                    activated: bool):
        payload = create_payload(create_user_params(first_name, last_name, username,
                                                    password, phone_no, email, image_url,
                                                    activated))
        return self.post(self.users_path, payload, self.content_type)

    def get_user(self) -> User:
        resp = self.get(self.users_path, '', self.content_type)
        if validate_response(resp):
            return User(i(resp, 'first_name'), i(resp, 'last_name'),
                        i(resp, 'username'), i(resp, 'password'),
                        i(resp, 'phone_no'), i(resp, 'image_url'),
                        i(resp, 'ref'), i(resp, 'email'),
                        i(resp, 'activated'), i(resp, 'created_at'))
        else:
            raise Exception(resp['status']['message'])

    def update_user(self, ref: str, first_name: str, last_name: str, username: str,
                    password: str, phone_no: str, email: str, image_url: str,
                    activated: bool):
        payload = create_payload(create_update_user_params(ref, first_name, last_name, username,
                                                           password, phone_no, email, image_url,
                                                           activated))
        return self.put(self.users_path, payload, self.content_type)

    def delete_user(self, user_ref: str):
        return self.delete(self.users_path, '', self.content_type)
