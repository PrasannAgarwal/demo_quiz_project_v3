import openai
import yaml

with open("config.yaml", "r") as stream:
    try:
        # print(yaml.safe_load(stream))
        openai.api_key = yaml.safe_load(stream)['API_KEY']
        print(openai.api_key)
    except yaml.YAMLError as exc:
        print(exc)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    # {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "generate a MCQ type question and answer on liverpool football club with 4 choices and difficulty level hard. Present answer in JSON format as follows: {question: question phrase, choices: list of choices, answer: list of answers} leave list of choices empty if no choices are asked in the question."}
  ]
)

print(completion.choices[0].message['content'])
