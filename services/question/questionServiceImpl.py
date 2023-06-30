from services.question.questionService import QuestionService
from services.question.createPromptServiceImpl import CreatePromptServiceImpl
from services.question.askQuestionServiceImpl import AskQuestionServiceImpl

class QuestionServiceImpl(QuestionService):
    def __init__(self):
        self.createPromptService = CreatePromptServiceImpl()
        self.askQuestionServiceImpl = AskQuestionServiceImpl()

    def generate_question(self, topic, difficulty, question_type, num_questions):
        # question = f"generate a {question_type} type question and answer on {topic} with "
        # if question_type == 'MCQ' or question_type == 'multiple correct answers':
        #     print(question_type)
        #     question = question + "4 choices and "
        # question = question + f"difficulty level {difficulty}."
        # question = question + "Present answer in JSON format as follows: {question: question phrase, choices: list of choices, answer: list of answers} leave list of choices empty if no choices are asked in the question."

        question = self.createPromptService.create_prompt(topic=topic, difficulty=difficulty, question_type=question_type, num_questions=num_questions)
        print(question)
        # completion = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #     {"role": "user", "content": question}
        #     ]
        # )
        # response = completion.choices[0].message["content"]
        # print(response)
        # response_json = json.loads(response)
        gpt_response = self.askQuestionServiceImpl.ask_question(question=question)
        return gpt_response