from services.responseValidator.responseValidatorService import ResponseValidatorService

class ResponseValidatorServiceImpl(ResponseValidatorService):

    def validateResponse(self, response_body):
        return True