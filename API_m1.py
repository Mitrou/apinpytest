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


# test API_m1.py
def test_data(self):
    self.result1 = choice(FIRST_NAMES)
    assert type(self.result1) in FIRST_NAMES