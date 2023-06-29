from services.question.createPromptService import CreatePromptService

class CreatePromptServiceImpl(CreatePromptService):

    def create_prompt(self, topic, difficulty, question_type):
        num_questions = 1
        question_type = question_type.lower()
        difficulty = difficulty.lower()
        topic = topic.lower()

        if question_type == 'fill':
            question_phrase = f'I want you to act as a fill in the blank question generator for students learning {topic}. Your task is to create {num_questions} questions with a list of sentences, each with a blank space where a word is missing. The student’s task is to fill in the blank with the correct word'
        if question_type == 'mcq':
            question_phrase = f'generate {num_questions} question with 4 choices with only one correct answer on {topic} with a '
        if question_type == 'multiple correct answers':
            question_phrase = f'generate {num_questions} question with 4 choices with multiple correct answers on {topic} with a '
        # question = f"{question_phrase} on {topic} with a "
        # if question_type == 'MCQ' or question_type == 'multiple correct answers':
        #     print(question_type)
        #     question = question + "4 choices and "
        question = question_phrase + f"{difficulty} difficulty level."
        question = question + ''' Present your answer in the followiing format: {"question": question phrase in quotes, "choices": list of choices enclosed in square brackets, "answer": list of answers enclosed in square brackets} leave list of choices empty if no choices are asked in the question.'''
        print("+++++++++++++++")
        print(question)
        print("+++++++++++++++")
        return question
        # return super().create_prompt(topic, difficulty, question_type)