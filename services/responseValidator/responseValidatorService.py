from abc import ABC, abstractmethod

class ResponseValidatorService(ABC):

    @abstractmethod
    def resp_validate(self, response_body, question_type, num_questions):
        pass
