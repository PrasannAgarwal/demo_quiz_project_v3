import openai
import yaml
import json
from services.validator.validationServiceImpl import ValidationServiceImpl
from services.question.questionServiceImpl import QuestionServiceImpl
from services.responseValidator.responseValidatorServiceImpl import ResponseValidatorServiceImpl
from flask_restful import Resource, reqparse


with open("config.yaml", "r") as stream:
    try:
        # print(yaml.safe_load(stream))
        openai.api_key = yaml.safe_load(stream)['API_KEY']
        # print(openai.api_key)
    except yaml.YAMLError as exc:
        print(exc)

class QuestionController(Resource):


    def __init__(self):
        print("Controller initialized")
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('question_type',
            required=True,
            help='This field cannot be left empty'
        )

        self.parser.add_argument('difficulty_level',
            required=True,
            help='This field cannot be left empty'
        )

        self.parser.add_argument('topic',
            required=True,
            help='This field cannot be left empty'
        )

        self.validationService = ValidationServiceImpl()
        self.questionService = QuestionServiceImpl()
        self.responseValidatorService = ResponseValidatorServiceImpl()

    def post(self):
        data = self.parser.parse_args()
        print("DATA in question controller")
        print(data)
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        self.validationService.validate(data=data)
        response_correct = False
        count = 0
        while not response_correct and count<5:
            response_body = self.questionService.generate_question(topic=data['topic'], difficulty=data['difficulty_level'], question_type=data['question_type'])

            response_correct = self.responseValidatorService.validateResponse(response_body=response_body)
            count -= 1
        return response_body


    # @staticmethod
    # def generate_question(question_type, difficulty, topic):
    #     question = f"generate a {question_type} type question and answer on {topic} with "
    #     if question_type == 'MCQ' or question_type == 'multiple correct answers':
    #         print(question_type)
    #         question = question + "4 choices and "
    #     question = question + f"difficulty level {difficulty}."
    #     question = question + "Present answer in JSON format as follows: {question: question phrase, choices: list of choices, answer: list of answers} leave list of choices empty if no choices are asked in the question."
    #     print(question)
    #     completion = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #         {"role": "user", "content": question}
    #         ]
    #     )
    #     response = completion.choices[0].message["content"]
    #     print(response)
    #     response_json = json.loads(response)
    #     return response_json
