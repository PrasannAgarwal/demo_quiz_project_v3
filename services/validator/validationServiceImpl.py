from services.validator.validationService import ValidationService
from services.validator.questionDifficultyValidator import QuestionDifficultyValidator
from services.validator.questionTypeValidator import QuestionTypeValidator
from services.validator.questionTopicValidator import QuestionTopicValidator

class ValidationServiceImpl(ValidationService):

    def __init__(self):
        self.validator_list = list()
        self.validator_list.append(QuestionDifficultyValidator())
        self.validator_list.append(QuestionTypeValidator())
        self.validator_list.append(QuestionTopicValidator())

    def validate(self, data):
        #to_implement
        #do with function programming
        try:
            for validator in self.validator_list:
                validator.validate()
        except Exception as e:
            return e
        return True