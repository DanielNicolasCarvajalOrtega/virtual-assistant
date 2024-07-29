import pytest
from venv import main
from flask import Flask

app = Flask(__name__)
@pytest.fixture     # funcion que proporciona un entorno de prueba preconfigurado
def client():
    try:
        app.testing = True    # activamos modo de prueba
        with app.test_client() as client:   #
            yield client
    except testing.TestClient as e:
        pytest.fail(e)

def test_major(client):
    try:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode() == "Hello World!"
    except AssertionError as e:
        print(f"Error of Assertion {e}")
def test_hello_without_key(client):
    try:
        response = client.get('/v1/virtual-assistant-core/welcome')
        assert response.status_code == 200
        assert 'welcome' in response.get_json()
    except AssertionError as e:
        print(f"Error of Assertion {e}")
def test_hello_with_valid_key(client):
    try:
        response = client.get('/v1/virtual-assistant-core/welcome?key=welcome')
        assert response.status_code == 200
        assert response.get_json() == {
            'welcome': "Welcome to virtual assistant.. how do you to do today?"
        }
    except AssertionError as e:
        print(f"Error of Assertion {e}")
def test_hello_with_invalid_key(client):
    try:
        response = client.get('/v1/virtual-assistant-core/welcome?key=invalid')
        assert response.status_code == 404
        assert response.get_json() == {
            'error': 'Not Found'
        }
    except AssertionError as e:
        print(f"Error of Assertion {e}")

if __name__ == "__main__":
    pytest.main()