class AssistantRepository:
    welcome: dict

    def __init__(self):
        self.welcome = {
            'welcome': "Welcome to virtual assistant.. how do you to do today?"

        }

    def get_welcome(self):
        return self.welcome
