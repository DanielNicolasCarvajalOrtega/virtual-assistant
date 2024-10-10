from app.model.Repositories import AssistantRepository


class AssistantService:

    def __init__(self):
        self.repository = AssistantRepository()

    def get_menu_speech(self):
        self.repository.get_menu_text_to_speech()

    def get_welcome_speech(self):
        return self.repository.get_welcome_text_to_speech()

    def get_welcome(self):
        return self.repository.get_welcome()

    def get_menu(self):
        return self.repository.get_menu()

    def get_handle_exception(self):
        return self.repository.handle_exception()

