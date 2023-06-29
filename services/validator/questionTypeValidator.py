from services.validator.validator import Validator
from services.validator.questionTypeEnum import QuestionTypes

class QuestionTypeValidator(Validator):

    def validate(self, data):
        print("Validating type")
        #check if Json contains key
        if 'question_type' not in data:
            raise NameError("No question_type found in the payload")
        if data.get('question_type') is None:
            raise ValueError("question_type value is empty in the payload")
        question_type = data['question_type'].lower()
        QuestionTypeSet = [questionType.value for questionType in QuestionTypes]
        if question_type not in QuestionTypeSet:
            raise ValueError(f"question_type can only be one of the following types: {'; '.join(QuestionTypeSet)}")
        #check if type part of enum three values
            #throw exception with message
        #to_implement