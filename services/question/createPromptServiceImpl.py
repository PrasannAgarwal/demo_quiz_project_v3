from services.question.createPromptService import CreatePromptService

class CreatePromptServiceImpl(CreatePromptService):

    def create_prompt(self, topic, difficulty, question_type):
        question = f"generate one {question_type} type question and answer on {topic} with "
        if question_type == 'MCQ' or question_type == 'multiple correct answers':
            print(question_type)
            question = question + "4 choices and "
        question = question + f"difficulty level {difficulty}."
        question = question + '''Present your answer in the followiing format: {"question": question phrase in quotes, "choices": list of choices enclosed in square brackets, "answer": list of answers enclosed in square brackets} leave list of choices empty if no choices are asked in the question.'''
        return question
        # return super().create_prompt(topic, difficulty, question_type)