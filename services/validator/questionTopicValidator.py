from services.validator.validator import Validator

class QuestionTopicValidator(Validator):
    def validate(self, data):
        print("Validating topic")
        if 'topic' not in data:
            raise NameError("No topic found in the payload")
        if data.get('topic') is None:
            raise ValueError("topic value is empty in the payload")
        #to_implement