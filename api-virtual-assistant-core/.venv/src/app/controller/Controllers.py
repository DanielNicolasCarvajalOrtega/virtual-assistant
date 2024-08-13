from flask import Flask, request, jsonify
from flask_injector import FlaskInjector, inject, singleton

from app.service.Services import AssistantService
from app.model.Repositories import AssistantRepository

app = Flask(__name__)


@app.route("/")
def major():
    return "Hello World!"


@app.route("/v1/virtual-assistant-core/welcome", methods=['GET'])
@inject
def hello(service: AssistantService):
    try:
        return service.get_welcome()

    except Exception as e:
        return f"error {e}"

@app.route("/v1/virtual-assistant-core/menu", methods=['GET'])
def menu_functions(service: AssistantService):
    try:
        key = request.args.get('key')
        if key:
            data = next((item for item in service.get_menu() if item["id"] == key), None)  # ITERAR SOBRE UNA ESTUCTURA DE DATOs
            if data:
                return jsonify({key: data})
            else:
                return jsonify({f"error": "Not Found"}), 404
        return service.get_menu()

    except:
        return service.get_handle_exception()


# Dependency configurations
def configure(binder):
    binder.bind(AssistantService, to=AssistantService(), scope=singleton)


if __name__ == "__main__":
    # app.run('localhost', 5005, debug=True)
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=True)
