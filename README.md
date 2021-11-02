# Nectar Python SDK

Nectar Python SDK is a wrapper that allows generation of STS compliant prepaid tokens using the Nectar API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this SDK.

```bash
pip install nectar_python_sdk
```

## Usage

```python
from nectar import Nectar

import datetime

# Get from the Nectar API Portal at https://portal.nectar.software/credentials
key = ''
secret = ''
nectar = Nectar(key, secret)

"""
User Endpoints
"""

# get user
print(nectar.get_user_factory().get_user())

# create user
first_name = 'first_name'
last_name = 'last_name'
username = 'username'
password = 'password'
phone_no = '0711100100'
email = 'email@email.co'
image_url = 'https://i.img.co/1.jpg'
activated = True

print(nectar.get_user_factory().create_user(first_name, last_name, username, password,
                                            phone_no, email, image_url, activated))

# update user
ref = 'f6080ca3-2b75-4beb-97d6-72f98082bdf5'
first_name = 'first_name_1'
last_name = 'last_name_2'
username = 'reayn3'
password = 'password'
phone_no = '0711100102'
email = 'email@email.com'
image_url = 'https://i.img.co/2.jpg'
activated = False

print(nectar.get_user_factory().update_user(ref, first_name, last_name, username, password,
                                            phone_no, email, image_url, activated))

"""
Token Endpoints
"""

# get token
print(nectar.get_token_factory().get_token('466d464c-eba1-4157-baa8-e18465d4b566'))

# generate electricity token
tid = datetime.datetime(2021, 10, 21, 11, 00)
amount = 10
random_no = 3
is_stid = False
drn = '12345678903'
config_ref = 'f6080ca3-2b75-4beb-97d6-72f98082bdf5'
debug = False

print(nectar.get_token_factory().generate_electricity_token(tid, amount, random_no, is_stid, drn, config_ref, debug))

# generate water token
print(nectar.get_token_factory().generate_water_token(tid, amount, random_no, is_stid, drn, config_ref, debug))

# generate gas token
print(nectar.get_token_factory().generate_gas_token(tid, amount, random_no, is_stid, drn, config_ref, debug))

# generate initiate meter test display 10
control = '68719476735'
manufacturer_code = '21'
print(nectar.get_token_factory()
      .generate_initiate_meter_test_display10_token(tid, control, manufacturer_code,
                                                    is_stid, drn, config_ref, debug))

# generate initiate meter test display 11
control = '268435455'
manufacturer_code = '1234'
print(nectar.get_token_factory()
      .generate_initiate_meter_test_display11_token(tid, control, manufacturer_code,
                                                    is_stid, drn, config_ref, debug))

# generate set maximum power limit token
maximum_power_limit = 100
print(nectar.get_token_factory().generate_set_maximum_power_limit_token(tid, maximum_power_limit,
                                                                        random_no, is_stid, drn, config_ref, debug))

# generate clear credit token
register = 0
print(nectar.get_token_factory().generate_clear_credit_token(tid, register, random_no,
                                                             is_stid, drn, config_ref, debug))

# generate set tariff rate token
tariff_rate = 10
print(nectar.get_token_factory().generate_set_tariff_rate_token(tid, tariff_rate, random_no,
                                                                is_stid, drn, config_ref, debug))

# generate set 1st section decoder key token
new_vending_key = '0abc12def3456789'
new_supply_group_code = '000046'
new_tariff_index = '01'
new_key_revision_no = 1
new_key_type = 0
new_key_expiry_no = 255
new_drn = '47500150231'
new_issuer_identification_no = '600727'
ro = 0
print(nectar.get_token_factory().generate_set_1st_section_decoder_key_token(tid, new_vending_key, new_supply_group_code,
                                                                            new_tariff_index, new_key_revision_no,
                                                                            new_key_type, new_key_expiry_no,
                                                                            new_drn, new_issuer_identification_no, ro,
                                                                            is_stid, drn, config_ref, debug))

# generate set 2nd section decoder key token
print(nectar.get_token_factory().generate_set_2nd_section_decoder_key_token(tid, new_vending_key, new_supply_group_code,
                                                                            new_tariff_index, new_key_revision_no,
                                                                            new_key_type, new_key_expiry_no,
                                                                            new_drn, new_issuer_identification_no, ro,
                                                                            is_stid, drn, config_ref, debug))

# generate clear tamper condition token
pad = 10
print(nectar.get_token_factory().generate_clear_tamper_condition_token(tid, pad, random_no, is_stid, drn,
                                                                       config_ref, debug))

# generate set maximum phase power unbalance limit token
mppul = 10
print(nectar.get_token_factory().generate_set_maximum_phase_power_unbalance_limit_token(tid, mppul, random_no, is_stid,
                                                                                        drn, config_ref, debug))

# generate set water meter factor token
wm_factor = 10
print(nectar.get_token_factory().generate_set_water_meter_factor_token(tid, wm_factor, random_no, is_stid,
                                                                       drn, config_ref, debug))

"""
Configurations
"""

# get configuration
print(nectar.get_configurations_factory().get_configuration(config_ref))

# activate configuration
print(nectar.get_configurations_factory().activate_configuration(config_ref))

# deactivate configuration
print(nectar.get_configurations_factory().deactivate_configuration(config_ref))

"""
Credentials
"""
print(nectar.get_credentials_factory().get_credentials('df0d307b-46fa-44bf-983f-8e2a780307ea'))
print(nectar.get_credentials_factory().activate_credentials('df0d307b-46fa-44bf-983f-8e2a780307ea'))
print(nectar.get_credentials_factory().deactivate_credentials('df0d307b-46fa-44bf-983f-8e2a780307ea'))

"""
Public Keys
"""
name = 'api public key'
key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAufC/0TyM8HBoIN0I8mpF MP7VXoc9S/O45Dyuv7XH+gQdMUaJQbzFt9WPH7WJHiLeuTk4kniEhPG4g5d16foq tzAzDRjKAFg0sIQp3uTdrAyJY3axAqY2oTqVNxxuHYmVc3E8LVcw5/4K74iy/hSd /TFMTlgqQ2uz2bOV0qI0dN8YqCqZTNgtE0/Z4Vx0y6HpYt7O0IWeCAZqTETfDjgp QXgzsLb72Z8ZAApVDVND+fTPTPLFkjYvzeOf9yPg3JLjVuNZdHE5PSkYkIYtSsL/ 8UzeUsVOWo8ECQI7b+VaRGXBdqWtR0qv0+lPeBrgoRWmJFwBjNfP/4GTeQh82HI7 ZIvQDighnEqQUaEumI3jEjs8Gh3hE2r6D2/SUCGvyH/JDp7esVkRpBdRvNWmIyTD GvVqYpyKj9giYa+Nh7P/ul8z0KpCnfCKIm1YT+ZrfRuAlLtkqTvBP+q7pqtI9ZTn 3gnxRbDrJ0CpN0e4u2lPnNCVwfc0EthcL+2rBf5k7aHYOt2+bD0RO2K9wql9NZ3E 98fexgN8aoZdVytrDEkSpyrJ6+4xT0CUMUcqofnAjec0rdONM0Poq3qYqtnpia1e fcWZlBCTmRGlaOlqfhuwQBLd+mSTqDMi9EIKCk7Ee+qGNZXH4vNm368QO1ff/RrZ DwtMD0YmgEKKwoTLPMur91MCAwEAAQ=='
activated = True

print(nectar.get_public_keys_factory().create_public_key(name, key, activated))
print(nectar.get_public_keys_factory().activate_public_keys('3c1a860a-051d-4e9c-810d-981aa03e9fff'))
print(nectar.get_public_keys_factory().deactivate_public_keys('f69941f9-c6e7-4842-99a0-452e0b473f2a'))

"""
Credits
"""

print(nectar.get_credits_factory().get_credits())
print(nectar.get_credits_factory().get_transactions())

"""
Notifications
"""

print(nectar.get_notifications_factory().get_notifications())

notification_ref = ''
status = False
timestamp = 1634886005

print(nectar.get_notifications_factory().set_notification_read_status(notification_ref, status, timestamp))

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
