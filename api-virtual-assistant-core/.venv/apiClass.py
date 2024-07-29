from flask import jsonify,request


class myApi:
    def __init__(self):
        self.data = {
            'welcome':"Welcome to virtual assistant.. how do you to do today?",

        }


    def getMessages(self):
        return jsonify(self.data)
