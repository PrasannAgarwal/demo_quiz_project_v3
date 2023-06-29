from services.validator.validator import Validator
from services.validator.questionDifficultyEnum import QuestionDifficulties

class QuestionDifficultyValidator(Validator):

    def validate(self, data):
        print("Validating difficulty")

        if 'difficulty_level' not in data:
            raise NameError("No difficulty_level found in the payload")
        if data.get('difficulty_level') is None:
            raise ValueError("difficulty_level value is empty in the payload")
        difficulty_level = data['difficulty_level'].lower()
        QuestionDifficultySet = [questionDifficulty.value for questionDifficulty in QuestionDifficulties]
        if difficulty_level not in QuestionDifficultySet:
            raise ValueError(f"difficulty_level can only be one of the following types: {'; '.join(QuestionDifficultySet)}")
        #to_implement