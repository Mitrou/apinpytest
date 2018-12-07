import requests
import pytest
import json
from random import choice
from random import choice

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201
NOT_FOUND = 404
INT_ERROR = 500

FIRST_NAMES = ('john', 'bob', 'sara', 'phenix', 'jordan', 'henry')
LAST_NAMES = ('benin', 'rosman', 'krudo', 'shemlin', 'lord', 'sams')
SENIORITY = ('junior', 'middle', 'profi', 'advanced', 'guru')
POSITIONS = ('tester', 'automation', 'developer', 'admin')

# TODO negatives:
# field types
# field length
# blank post
# +1 to blank till actual
# +1 above actual
# +10 above actual

# TODO data/scenarios
# POS 5 valid bodies for parametrization
# NEG blank body
# NEG 2 one item body
# NEG 2 with INT for each element
# NEG 2 with special symbols for each element
# NEG 2 with 10k string for each element
# NEG 1 10 elements in body


# test API_m1.py
def test_data(self):
    self.result1 = choice(FIRST_NAMES)
    assert type(self.result1) in FIRST_NAMES