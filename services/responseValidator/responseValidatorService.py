from abc import ABC, abstractmethod

class ResponseValidatorService(ABC):

    @abstractmethod
    def validateResponse(self, response_body):
        pass
