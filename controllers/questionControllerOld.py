import openai
import yaml
import json

with open("config.yaml", "r") as stream:
    try:
        # print(yaml.safe_load(stream))
        openai.api_key = yaml.safe_load(stream)['API_KEY']
        print(openai.api_key)
    except yaml.YAMLError as exc:
        print(exc)

class QuestionController:

    @staticmethod
    def generate_question(question_type, difficulty, topic):
        question = f"generate a {question_type} type question and answer on {topic} with "
        if question_type == 'MCQ' or question_type == 'multiple correct answers':
            print(question_type)
            question = question + "4 choices and "
        question = question + f"difficulty level {difficulty}."
        question = question + "Present answer in JSON format as follows: {question: question phrase, choices: list of choices, answer: list of answers} leave list of choices empty if no choices are asked in the question."
        print(question)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": question}
            ]
        )
        response = completion.choices[0].message["content"]
        print(response)
        response_json = json.loads(response)
        return response_json
