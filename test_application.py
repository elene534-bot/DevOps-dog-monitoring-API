import pytest
from application import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_get_all_dogs(client):
    response = client.get('/dogs')
    assert response.status_code == 200
    assert response.json["total"] == 2

def test_high_aggression_dogs(client):
    response = client.get('/dogs/high-aggression')
    assert response.status_code == 200
    assert response.json["count"] == 1
    assert response.json["dogs"][0]["breed"] == "გერმანული ნაგაზი"