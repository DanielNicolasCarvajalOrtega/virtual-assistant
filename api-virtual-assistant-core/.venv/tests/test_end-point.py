import pytest
from venv import main
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_major(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello World!"

def test_hello_without_key(client):
    response = client.get('/v1/virtual-assistant-core/welcome')
    assert response.status_code == 200
    assert 'welcome' in response.get_json()

def test_hello_with_valid_key(client):
    response = client.get('/v1/virtual-assistant-core/welcome?key=welcome')
    assert response.status_code == 200
    assert response.get_json() == {
        'welcome': "Welcome to virtual assistant.. how do you to do today?"
    }

def test_hello_with_invalid_key(client):
    response = client.get('/v1/virtual-assistant-core/welcome?key=invalid')
    assert response.status_code == 404
    assert response.get_json() == {
        'error': 'Not Found'
    }

if __name__ == "__main__":
    pytest.main()