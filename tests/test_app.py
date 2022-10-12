import json

def test_index(app, client):
    del app
    res = client.get('/welcome')
    assert res.status_code == 200
    expected = {'message': 'Welcome to Pizza House'}
    assert json.loads(res.data) == expected

def test_addorder(app, client):
    del app
    res = client.post('/order', json={'order': ['Pizza1', 'Pizza2']})
    assert res.status_code == 200
    if res.status_code == 200:
        assert json.loads(res.data)['order_id'] is not None


def test_getorders(app, client):
    del app
    res = client.get('/getorders')
    j = json.loads(res.data)
    assert res.status_code == 200
    expected = 200
    assert res.status_code == expected

def test_getorder(app, client):
    del app
    res = client.get('/getorders/5f5e5a5b5e5b5a5b5e5b5a5b')
    j = json.loads(res.data)
    assert res.status_code == 404
    expected = 404
    assert res.status_code == expected


