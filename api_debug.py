import requests
import pytest
import json
from random import choice
import random
import string
from config import *

get_p_responce = requests.get(url)
status_code_to_test = get_p_responce.status_code
json_to_operate = get_p_responce.json()['candidates']
print(json_to_operate)

print(dict(json_to_operate[0]).get('id'))
print(dict(json_to_operate[0]))
for i in json_to_operate:
    fff.append(i['id'])
#    print(i['id'])
'''
print(fff)
payload = '{"name": "value1", "position": "value1"}'
r = requests.post(url, data = json.dumps(json.loads(payload)), headers = correct_header)
print(r.status_code, r.reason, r.text)

for i in fff:
    url_2_del = url + '/' + str(i)
    d = requests.delete(url_2_del)
    print(d.status_code, d.reason, d.text)

'''