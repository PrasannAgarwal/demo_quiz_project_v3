from abc import ABC, abstractmethod

class ResponseValidator(ABC):

    @abstractmethod
    def resp_validate(self, responseJson, question_type, num_questions):
        pass