from flask import Flask, request, jsonify
from apiClass import myApi

app = Flask(__name__)
api = myApi()


@app.route("/")
def major():
    return "Hello World!"


@app.route("/v1/virtual-assistant-core/welcome", methods=['GET'])
def hello():
    try:
        key = request.args.get('key')  # obtener parametro key de la URL
        if key:
            data = api.data.get(key)  # si esa key exite en data obitiene el valor
            if data:
                return jsonify({key: data})  # retorna en formato json atributo y valor
            else:
                return jsonify({f"error": "Not Found"}), 404
        return api.getMessages()

    except Exception as e:
        return f"error {e}"


@app.route("/v1/virtual-assistant-core/menu", methods=['GET'])
def menu_functions():
    try:
        key = request.args.get('key')
        if key:
            data = next((item for item in api.menu if item["id"] == key), None) # ITERAR SOBRE UNA ESTUCTURA DE DATOs
            if data:
                return jsonify({key: data})
            else:
                return jsonify({f"error": "Not Found"}), 404
        return api.getmenu()
    except:
        return api.handle_exception()


if __name__ == "__main__":
    app.run(debug=True)
