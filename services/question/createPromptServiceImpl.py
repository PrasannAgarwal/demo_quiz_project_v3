from services.question.createPromptService import CreatePromptService

class CreatePromptServiceImpl(CreatePromptService):

    def create_prompt(self, topic, difficulty, question_type, num_questions):
        # num_questions = 1
        question_type = question_type.lower()
        difficulty = difficulty.lower()
        topic = topic.lower()

        if question_type == 'fill':
            question_phrase = f'I want you to act as a fill in the blank question generator for students learning {topic}. Your task is to create {num_questions} question{"s" if num_questions>1 else ""} with a blank space where a word is missing. The student’s task is to fill in the blank with the correct word'
        if question_type == 'mcq':
            # question_phrase = f'generate {num_questions} question{"s" if num_questions>1 else ""} with 4 choices with only one correct answer on {topic} with a '
            question_phrase = f'I want you to act as a multiple choice question generator for students learning {topic}. Your task is to create {num_questions} question{"s" if num_questions>1 else ""} and provide with 4 choices for {"each" if num_questions>1 else "the"} question. Just one answer is the correct one. The student’s task is to select the correct answer.'
        if question_type == 'multiple correct answers':
            # question_phrase = f'generate {num_questions} question{"s" if num_questions>1 else ""} with 4 choices with multiple correct answers on {topic} with a '
            question_phrase = f'I want you to act as a multiple choice question generator for students learning {topic}. Your task is to create {num_questions} question{"s" if num_questions>1 else ""} and provide with 4 choices for {"each" if num_questions>1 else "the"} question. Multiple choices can be the correct answers. The student’s task is to select all the correct answers.'
        # question = f"{question_phrase} on {topic} with a "
        # if question_type == 'MCQ' or question_type == 'multiple correct answers':
        #     print(question_type)
        #     question = question + "4 choices and "
        question = question_phrase + f"{difficulty} difficulty level."
        output_json_format = '''
         Present your answer in the following format:
            {
                "questions": [
                    {
                        "question_id" : ..,
                        "question": question phrase in quotes,
                        "choices": [
                            {
                            "choice_id": ..,
                            "choice": choice
                            },
                            ...
                        ]
                        "answer": list of answers enclosed in square brackets
                    },
                    ...
                ]
            }

         Leave list of choices empty if no choices are asked in the question.
         '''
        # question = question + ''' Present your answer in the followiing format: "question number" :{"question": question phrase in quotes, "choices": list of choices enclosed in square brackets, "answer": list of answers enclosed in square brackets} leave list of choices empty if no choices are asked in the question.'''
        question = question + output_json_format
        print("+++++++++++++++")
        print(question)
        print("+++++++++++++++")
        return question
        # return super().create_prompt(topic, difficulty, question_type)