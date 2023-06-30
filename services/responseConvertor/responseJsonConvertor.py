from abc import ABC, abstractmethod

class ResponseJsonConvertor(ABC):

    @abstractmethod
    def resp_json_convertor(self, responseBody):
        pass