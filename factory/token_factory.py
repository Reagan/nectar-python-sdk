from factory.base import Base

from datetime import datetime
from factory.base import create_payload
from factory.base import f


class TokenFactory(Base):

    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)
        self.token_path = "/v1/tokens"

    def get_token(self, token_ref: str):
        path_args = 'ref={}'.format(token_ref)
        return self.get(self.token_path, path_args, self.content_type)

    def generate_electricity_token(self, token_id: datetime, amount: float,
                                   random_no: int, is_stid: bool,
                                   drn: str, config_ref: str,
                                   debug: bool):
        payload = create_payload({
            'class': '0',
            'subclass': '0',
            'token_id': f(token_id),
            'amount': amount,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_water_token(self, token_id: datetime, amount: float,
                             random_no: int, is_stid: bool,
                             drn: str, config_ref: str,
                             debug: bool):
        payload = create_payload({
            'class': '0',
            'subclass': '1',
            'token_id': f(token_id),
            'amount': amount,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_gas_token(self, token_id: datetime, amount: float,
                           random_no: int, is_stid: bool,
                           drn: str, config_ref: str,
                           debug: bool):
        payload = create_payload({
            'class': '0',
            'subclass': '2',
            'token_id': f(token_id),
            'amount': amount,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_initiate_meter_test_display10_token(self, token_id: datetime, control: str,
                                                     manufacturer_code: str, is_stid: bool,
                                                     drn: str, config_ref: str, debug: bool):
        payload = create_payload({
            'class': '1',
            'subclass': '0',
            'token_id': f(token_id),
            'control': control,
            'manufacturer_code': manufacturer_code,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug
        })

        return self.post(self.token_path, payload, self.content_type)

    def generate_initiate_meter_test_display11_token(self, token_id: datetime, control: str,
                                                     manufacturer_code: int, is_stid: bool, drn: str,
                                                     config_ref: str, debug: bool):
        payload = create_payload({
            'class': '1',
            'subclass': '1',
            'token_id': f(token_id),
            'control': control,
            'manufacturer_code': manufacturer_code,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug
        })

        return self.post(self.token_path, payload, self.content_type)

    def generate_set_maximum_power_limit_token(self, token_id: datetime, maximum_power_limit: int,
                                               random_no: int, is_stid: bool, drn: str,
                                               config_ref: str, debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '0',
            'token_id': f(token_id),
            'maximum_power_limit': maximum_power_limit,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })

        return self.post(self.token_path, payload, self.content_type)

    def generate_clear_credit_token(self, token_id: datetime, register: int,
                                    random_no: int, is_stid: bool, drn: str,
                                    config_ref: str, debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '1',
            'token_id': f(token_id),
            'register': register,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_set_tariff_rate_token(self, token_id: datetime, tariff_rate: int,
                                       random_no: int, is_stid: bool, drn: str,
                                       config_ref: str, debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '2',
            'token_id': f(token_id),
            'tariff_rate': tariff_rate,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_set_1st_section_decoder_key_token(self, token_id: datetime, new_vending_key: str,
                                                   new_supply_group_code: str, new_tariff_index: str,
                                                   new_key_revision_no: int,
                                                   new_key_type: int, new_key_expiry_no: int, new_drn: str,
                                                   new_issuer_identification_no: str, ro: int, is_stid: bool,
                                                   drn: str, config_ref: str, debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '3',
            'token_id': token_id,
            'new_vending_key': new_vending_key,
            'new_supply_group_code': new_supply_group_code,
            'new_tariff_index': new_tariff_index,
            'new_key_revision_no': new_key_revision_no,
            'new_key_type': new_key_type,
            'new_key_expiry_no': new_key_expiry_no,
            'new_drn': new_drn,
            'new_issuer_identification_no': new_issuer_identification_no,
            'ro': ro,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_set_2nd_section_decoder_key_token(self, token_id: datetime, new_vending_key: str,
                                                   new_supply_group_code: str, new_tariff_index: str,
                                                   new_key_revision_no: str, new_key_type: str, new_key_expiry_no: str,
                                                   new_drn: str, new_issuer_identification_no: str, ro: int,
                                                   is_stid: bool, drn: str, configRef: str,
                                                   debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '4',
            'token_id': token_id,
            'new_vending_key': new_vending_key,
            'new_supply_group_code': new_supply_group_code,
            'new_tariff_index': new_tariff_index,
            'new_key_revision_no': new_key_revision_no,
            'new_key_type': new_key_type,
            'new_key_expiry_no': new_key_expiry_no,
            'new_drn': new_drn,
            'new_issuer_identification_no': new_issuer_identification_no,
            'ro': ro,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': configRef,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_clear_tamper_condition_token(self, token_id: datetime, pad: int,
                                              random_no: int, is_stid: bool, drn: str, config_ref: str, debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '5',
            'token_id': token_id,
            'pad': pad,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_set_maximum_phase_power_unbalance_limit_token(self, token_id: datetime,
                                                               mppul: int, random_no: int,
                                                               is_stid: bool, drn: str, config_ref: str, debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '6',
            'token_id': token_id,
            'mppul': mppul,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)

    def generate_set_water_meter_factor_token(self, token_id: datetime, wm_factor: int,
                                              random_no: int, is_stid: bool,
                                              drn: str, config_ref: str,
                                              debug: bool):
        payload = create_payload({
            'class': '2',
            'subclass': '7',
            'token_id': token_id,
            'wm_factor': wm_factor,
            'random_no': random_no,
            'is_stid': is_stid,
            'drn': drn,
            'config_ref': config_ref,
            'debug': debug,
        })
        return self.post(self.token_path, payload, self.content_type)
