from flask import Flask, request, jsonify
from flask_injector import inject

from app.service import AssistantService

app = Flask(__name__)


@app.route("/")
def major():
    return "Hello World!"


@app.route("/v1/virtual-assistant-core/welcome", methods=['GET'])
@inject
def hello(service: AssistantService):
    try:
        key = request.args.get('key')  # obtener parametro key de la URL
        print(key)
        if key:
            data = service.get_welcome().get(key)  # si esa key exite en data obitiene el valor
            if data:
                return jsonify({key: data})  # retorna en formato json atributo y valor
            else:
                return jsonify({f"error": "Not Found"}), 404
        return service.get_welcome()

    except Exception as e:
        return f"error {e}"


if __name__ == "__main__":
    app.run(debug=True)
