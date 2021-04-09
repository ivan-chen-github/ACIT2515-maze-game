import json

def test_index(app, client):
    """test '/' route for 200 ok"""
    res = client.get('/')
    assert res.status_code == 200
