from enum import Enum
from utils.payload import Payload
from datetime import datetime

import secrets
import hmac
import hashlib
import base64
import requests
import json


class Http(Enum):
    GET = 1
    POST = 2
    DELETE = 3
    PUT = 4


def generate_hmac_auth(secret: str, verb: Http, path: str,
                       md5: str, content_type: str, date: str, nonce: str) -> str:
    content_str = verb.name.upper() + (path[
                                      :path.index('?')] if '?' in path else path) + md5 + content_type + date + nonce
    message = content_str.encode()
    return base64.b64encode(hmac.new(secret.encode(), message, hashlib.sha256).hexdigest().encode()).decode("utf-8")


def generate_nonce() -> str:
    return secrets.token_hex(15)


def md5(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest().upper()


def create_payload(params: dict) -> Payload:
    return Payload(params)


def is_valid(resp: dict) -> bool:
    if isinstance(resp['status'], int):
        return resp['status'] == 200
    elif isinstance(resp['status'], dict):
        return resp['status']['code'] == 200


def validated_resp(resp: dict) -> dict:
    if is_valid(resp):
        return resp
    elif isinstance(resp['status'], int):
        raise Exception('{} {}'.format(resp['error'], resp['path']))
    elif isinstance(resp['status'], dict):
        raise Exception(resp['status']['message'])


def e(resp: dict, elem: str) -> str:
    return resp['data']['data'][elem]


def f(token_id: datetime) -> str:
    return token_id.strftime("%Y-%m-%dT%H:%M")


class Base:
    base_url = "https://api.nectar.software"

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret
        self.content_type = "application/json"

    def post(self, path: str, payload: Payload, content_type: str) -> dict:
        nonce = generate_nonce()
        curr_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        generated_hmac = generate_hmac_auth(self.secret, Http.POST, path, md5(payload.to_json()), content_type,
                                            curr_date, nonce)
        content, headers = self.prepare_request(generated_hmac, content_type, md5(payload.to_json()), curr_date, nonce,
                                                payload)
        return validated_resp(requests.post("{}{}".format(self.base_url, path), data=content, headers=headers).json())

    def get(self, path: str, path_args: str, content_type: str) -> dict:
        nonce = generate_nonce()
        curr_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        generated_hmac = generate_hmac_auth(self.secret, Http.GET, path, md5(''), content_type, curr_date, nonce)
        content, headers = self.prepare_request(generated_hmac, content_type, md5(''), curr_date, nonce)
        return validated_resp(requests.get("{}{}?{}".format(self.base_url, path, path_args), headers=headers).json())

    def delete(self, path: str, path_args: str, content_type: str) -> dict:
        nonce = generate_nonce()
        curr_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        generated_hmac = generate_hmac_auth(self.secret, Http.DELETE, path, md5(''), content_type, curr_date, nonce)
        content, headers = self.prepare_request(generated_hmac, content_type, md5(''), curr_date, nonce)
        return validated_resp(
            requests.delete("{}{}?{}".format(self.base_url, path, path_args), data=content, headers=headers).json())

    def put(self, path: str, payload: Payload, content_type: str) -> dict:
        nonce = generate_nonce()
        curr_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        payload_str = payload.to_json() if payload else ''
        generated_hmac = generate_hmac_auth(self.secret, Http.PUT, path, md5(payload_str), content_type,
                                            curr_date, nonce)
        content, headers = self.prepare_request(generated_hmac, content_type, md5(payload_str), curr_date, nonce,
                                                payload)
        return validated_resp(requests.put("{}{}".format(self.base_url, path), data=content, headers=headers).json())

    def prepare_request(self, hmac: str, content_type: str, md5: str,
                        date: str, nonce: str, payload: Payload = None) -> tuple:
        content = json.dumps(payload.params).encode('utf-8') if payload else ''
        headers = {
            "Authorization": "NECTAR {}:{}".format(self.key, hmac),
            "Content-type": content_type,
            "Content-MD5": md5,
            "Date": date,
            "nonce": nonce,
            "User-Agent": "nectar-python-sdk"
        }
        return content, headers
