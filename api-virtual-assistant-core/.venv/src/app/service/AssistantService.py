from flask_injector import inject

from app.model import AssistantRepository


class AssistantService:
    repository: AssistantRepository

    @inject
    def __init__(self, repository: AssistantRepository):
        self.repository = repository

    def get_welcome(self):
        return self.repository.get_welcome()
