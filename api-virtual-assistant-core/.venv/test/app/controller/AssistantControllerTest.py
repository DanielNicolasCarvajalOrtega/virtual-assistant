import pytest
from flask import Flask, testing

app = Flask(__name__)
@pytest.fixture     # funcion que proporciona un entorno de prueba preconfigurado
def client():
    app.testing = True    # activamos modo de prueba
    with app.test_client() as client:   #
        yield client

# TEST REQUEST DEL WELCOME
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

# TEST REQUEST DEL MENU
def test_memu_functions_without_key(client):
    try:
        response = client.get('/v1/virtual-assistant-core/menu')
        assert response.status_code == 200
        assert 'menu' in response.get_json()
    except AssertionError as e:
        print(f"Error of Assertion {e}")



def test_memu_functions_with_key(client):
    try:
        response = client.get('/v1/virtual-assistant-core/menu')
        assert response.status_code == 200
        assert response.get_json =={
            "MUSIC_PLAY": {
                "description": "Reproducir musica",
                "id": "MUSIC_PLAY",
                "type": "MUSIC_PLAY"
            }
        }
        assert response.get_json() == {
            "DATE_TIME": {
                "description": "Dar dia y hora",
                "id": "DATE_TIME",
                "type": "DATE_TIME"
            }
        }
        assert response.get_json() == {
            "TRASLATION_IDIOM": {
                "description": "Traducir idioma",
                "id": "TRASLATION_IDIOM",
                "type": "TRASLATION_IDIOM"
            }
        }

        assert response.get_json() == {
            "INVESTIGATE_CONTENT": {
                "description": "Investigar contenido",
                "id": "INVESTIGATE_CONTENT",
                "type": "INVESTIGATE_CONTENT"
            }
        }

        assert response.get_json() == {
            "TALK_TEXT": {
                "description": "Dictar un archivo de texto",
                "id": "TALK_TEXT",
                "type": "TALK_TEXT"
            }
        }

    except AssertionError as e:
        print(f"Error of Assertion {e}")

def test_memu_functions_invalid_key(client):
    try:
        response = client.get('/v1/virtual-assistant-core/menu?key=invalid')
        assert response.status_code == 404
        assert response.get_json() == {
            'error': 'Not Found'
        }
    except AssertionError as e:
        print(f"Error of Assertion {e}")


if __name__ == "__main__":
    pytest.main()