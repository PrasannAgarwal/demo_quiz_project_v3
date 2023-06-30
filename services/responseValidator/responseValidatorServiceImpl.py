from services.responseValidator.responseValidatorService import ResponseValidatorService
from services.responseValidator.responseJsonValidator import ResponseJsonValidator

class ResponseValidatorServiceImpl(ResponseValidatorService):
    def __init__(self):
        print("Initializing response validators")
        self.response_validator_list = list()
        self.response_validator_list.append(ResponseJsonValidator())

    def resp_validate(self, response_body, question_type, num_questions):
        #to_implement
        #do with function programming
        try:
            print("Response Validation services starting")
            # print(self.validator_list)
            for respValidator in self.response_validator_list:
                # print(validator)
                respValidator.resp_validate(response_body, question_type, num_questions)
        except Exception as e:
            raise e