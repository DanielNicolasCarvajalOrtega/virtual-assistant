from src.app.model.Repositories import AssistantRepository
import pyttsx3


class config:
    def __init__(self):
        self.repo = AssistantRepository()
        self.engine = pyttsx3.init()
        self.voice = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voice[3].id)
        self.engine.getProperty('rate')
        self.engine.setProperty('rate',160)
        self.engine.setProperty('volume',40)

    def speak(self):
        welcome_speech = str(self.repo.get_welcome_text_to_speech())
        print(welcome_speech)
        self.engine.say(welcome_speech)
        menu_speech = str(self.repo.get_menu_text_to_speech())
        print(menu_speech)
        self.engine.say(menu_speech)
        self.engine.runAndWait()



text_speech = config()
text_speech.speak()


