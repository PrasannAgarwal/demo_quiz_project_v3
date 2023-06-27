from flask import Flask
from flask import request, jsonify
from flask_restful import Api
import yaml
from controllers.questionController import QuestionController

# with open("config.yaml", "r") as stream:
#     try:
#         # print(yaml.safe_load(stream))
#         database_uri = yaml.safe_load(stream)['DATABASE_URI']
#     except yaml.YAMLError as exc:
#         print(exc)

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Secret_key"

api = Api(app)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


# @app.route('/ask_gpt', methods=['POST'])
# def ask_gpt():
#    data = request.get_json(force=True)
#    res = questionController.generate_question(data['question_type'], data['difficulty_level'], data['topic'])
#    return res


api.add_resource(QuestionController, '/ask_gpt')





if __name__ == "__main__":
  app.debug = True
  app.run()