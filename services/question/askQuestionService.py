from abc import ABC, abstractmethod

class AskQuestionService(ABC):

    @abstractmethod
    def ask_question(self, question):
        pass
