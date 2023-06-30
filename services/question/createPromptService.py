from abc import ABC, abstractmethod

class CreatePromptService(ABC):

    @abstractmethod
    def create_prompt(self, topic, difficulty, question_type, num_questions):
        pass
