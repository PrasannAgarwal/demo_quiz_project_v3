from services.responseValidator.responseValidator import ResponseValidator

class ResponseJsonValidator(ResponseValidator):

    def resp_validate(self, responseJson, question_type, num_questions):
        '''
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
        '''
        try:
            print("=============================================")
            print("THIS IS RESPONSE JSON")
            print(responseJson)
            print("=============================================")
            if 'questions' not in responseJson:
                raise ValueError('Invalid response Json')
                # raise ValueError("response Json does not contain key parameter 'questions'.")
            if responseJson.get('questions') is None:
                # raise ValueError("response Json does not contain value for 'questions' key.")
                raise ValueError('Invalid response Json')
            if not isinstance(responseJson['questions'], list):
                raise ValueError('Invalid response json')
            if len(responseJson['questions'])!=num_questions:
                raise ValueError("Invalid response Json")
            cnt = 1
            for question in responseJson['questions']:
                if 'question_id' not in question or 'question' not in question or 'choices' not in question or 'answer' not in question:
                    raise ValueError("Invalid response json")
                if not (isinstance(question['question_id'], int) and isinstance(question['question'], str) and isinstance(question['choices'], list) and isinstance(question['answer'], list)):
                    raise ValueError("Invalid response json")
                if question['question_id']!=cnt:
                    raise ValueError("Invalid response json")
                if question_type != 'fill':
                    if len(question['choices'])!=4:
                        raise ValueError("Invalid response json")
                    choice_cnt = 1
                    for choice in question['choices']:
                        if (not isinstance(choice['choice_id'], int)) or choice['choice_id']!=choice_cnt:
                            raise ValueError("Invalid response json")
                        if not isinstance(choice['choice'],str):
                            raise ValueError("Invalid response json")
                        choice_cnt += 1
                cnt += 1
        except Exception as e:
            raise e