from flask import jsonify, Flask
from datetime import datetime

app = Flask(__name__)

class myApi:
    def __init__(self):
        self.data = {
            'welcome': "Welcome to virtual assistant.. how do you to do today?"

        }
        self.menu = [

                {
                    "id": "MUSIC_PLAY",
                    "type": "MUSIC_PLAY",
                    "description": "Reproducir musica"
                },
                {
                    "id": "DATE_TIME",
                    "type": "DATE_TIME",
                    "description": "Dar dia y hora"
                },
                {
                    "id": "TRASLATION_IDIOM",
                    "type": "TRASLATION_IDIOM",
                    "description": "Traducir idioma"
                },
                {
                    "id": "INVESTIGATE_CONTENT",
                    "type": "INVESTIGATE_CONTENT",
                    "description": "Investigar contenido"
                },
                {
                    "id": "TALK_TEXT",
                    "type": "TALK_TEXT",
                    "description": "Dictar un archivo de texto"
                }
        ]

    def __str__(self):
        return f"menu = {self.menu}"

    def getMessages(self):
        return jsonify(self.data)

    def getmenu(self):
        return jsonify(self.menu)

    @app.errorhandler(500)
    def handle_exception(e):
        response = {
            "status": "500",
            "description": "Internal Server Error",
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%SS"),
            "details": str(e)
        }

        return jsonify(response), 500
