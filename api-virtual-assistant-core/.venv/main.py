from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def major():
    return "Hello World!"

@app.route("/v1/virtual-assistant-core/welcome", methods=['GET'])
def hello():
    saludar = {
        'welcome': "Welcome to virtual assistant.. how do you to do today?"
    }
    return jsonify(saludar)


if __name__ == "__main__":
    app.run()