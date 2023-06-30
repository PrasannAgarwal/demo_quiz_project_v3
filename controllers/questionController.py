import openai
import yaml
import json
from services.validator.validationServiceImpl import ValidationServiceImpl
from services.question.questionServiceImpl import QuestionServiceImpl
from services.responseValidator.responseValidatorServiceImpl import ResponseValidatorServiceImpl
from services.responseConvertor.responseJsonConvertorImpl import ResponseJsonConvertorImpl
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
        self.responseJsonConvertorService = ResponseJsonConvertorImpl()

    def post(self):
        print("DATA in question controller")
        # print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        try:
            data = self.parser.parse_args()
            print(data)
            self.validationService.validate(data=data)
        except Exception as e:
            return {"message": "Invalid payload"}, 400
        try:
            response_correct = False
            count = 0
            num_questions = 1
            num_retries = 5
            while not response_correct and count < num_retries:
                response_body = self.questionService.generate_question(topic=data['topic'], difficulty=data['difficulty_level'], question_type=data['question_type'], num_questions=num_questions)
                try:
                    response_json = self.responseJsonConvertorService.resp_json_convertor(responseBody=response_body)
                    self.responseValidatorService.validateResponse(response_json=response_json, question_type = data['question_type'], num_questions=num_questions)
                    response_correct = True
                    count +=1
                except Exception as e:
                    print(e)
                    response_correct = False
                    count += 1
            if not response_correct:
                return {"message": "Unable to fulfill request"}, 500
            return response_json, 200
        except Exception as e:
            return {"message": "Unable to fulfill request"}, 500


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
