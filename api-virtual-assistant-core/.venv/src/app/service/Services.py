from app.model.Repositories import AssistantRepository


class AssistantService:

    def __init__(self):
        self.repository = AssistantRepository()

    def get_welcome(self):
        return self.repository.get_welcome()

