import requests

url = 'http://maps.googleapis.com/maps/api/directions/json'
"""
params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below

print(data)"""

def test_qwe_qwe():
    a = 1
    assert a==1
    return a

def test_qwe_2():
    b = test_qwe_qwe()
    assert b == 1