import requests
import pytest
import json
from random import choice
import random
import string


DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201
NOT_FOUND = 404
INT_ERROR = 500

FIRST_NAMES = ('john', 'paul', 'ringo', 'george', 'phil', 'pete')
LAST_NAMES = ('lennon', 'mccartney', 'starr', 'harrison', 'spector', 'best')
SENIORITY = ('junior', 'middle', 'senior', 'tech lead')
POSITIONS = ('tester', 'dev-ops', 'developer', 'admin')
empty_str = ''
base_url = 'http://qainterview.cogniance.com/candidates'


@pytest.fixture()
def json_body_generator(arg):
    thousand_chars_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10000)])
    ten_chars_spec_symbols = ''.join([random.choice(string.punctuation) for n in range(10)])
    fl_name_positive = choice(FIRST_NAMES) + ' ' + choice(LAST_NAMES)
    position_positive = choice(SENIORITY) + ' ' + choice(POSITIONS)
    request_body = ''
    if arg == 'POS':
        request_body = '{"name": "'+ fl_name_positive + '", "position": "' + position_positive + '"}'
    elif arg == 'N_int_name':
        request_body = '{"name": "'+ '123' + '", "position": "' + position_positive + '"}'
    elif arg == 'N_int_position':
        request_body = '{"name": "'+ fl_name_positive + '", "position": "' + '123' + '"}'
    elif arg == 'N_10k_chars_name':
        request_body = '{"name": "'+ thousand_chars_str + '", "position": "' + position_positive + '"}'
    elif arg == 'N_10k_chars_position':
        request_body = '{"name": "'+ fl_name_positive + ', "position": "' + thousand_chars_str + '"}'
    elif arg == 'N_10_chars_spec_symbols':
        request_body = '{"name": "'+ ten_chars_spec_symbols + '", "position": "' + ten_chars_spec_symbols + '"}'
    elif arg == 'N_blank_whole':
        request_body = '{}'
    elif arg == 'N_blank_values':
        request_body = '{"name": ,"position": }'
    elif arg == 'N_blank_keys':
        request_body = '{ :"'+ fl_name_positive + '", :"' + thousand_chars_str + '"}'
    elif arg == 'N_no_name':
        request_body = '{"position": "' + position_positive + '"}'
    elif arg == 'N_no_position':
        request_body = '{"name": "' + fl_name_positive + '"}'
    elif arg == 'N_tree_elements':
        request_body = '{"name": "value1", "position": "value1", "key3": "value3"}'
    return request_body

#def check_get_all_and_existing_data():


# TODO common scenario:
# set up with existing data check
# post and store posted data after check POST by GET
# clean up API


print(json_body_generator('POS'))
print(json_body_generator('N_int_name'))
print(json_body_generator('N_int_position'))
print(json_body_generator('N_10k_chars_name'))
print(json_body_generator('N_10k_chars_position'))
print(json_body_generator('N_10_chars_spec_symbols'))
print(json_body_generator('N_blank_whole'))
print(json_body_generator('N_blank_values'))
print(json_body_generator('N_blank_keys'))
print(json_body_generator('N_no_name'))
print(json_body_generator('N_no_position'))
print(json_body_generator('N_tree_elements'))

