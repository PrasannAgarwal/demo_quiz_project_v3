from abc import ABC, abstractmethod

class QuestionService(ABC):

    @abstractmethod
    def generate_question(self, topic, difficulty, question_type):
        pass
