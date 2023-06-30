from services.question.askQuestionService import AskQuestionService
import openai
import json

class AskQuestionServiceImpl(AskQuestionService):
    def ask_question(self, question):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": question}
            ]
        )
        response = completion.choices[0].message["content"]
        print(response)
        return response
        # response_json = json.loads(response)
        # return response_json
        # return super().ask_question(question)