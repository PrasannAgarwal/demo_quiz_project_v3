#make a POST request
import requests
dictToSend = {
    "question_type": "fill",
    "difficulty_level": "medium",
    "topic": "xyz"
}
res = requests.post('http://127.0.0.1:5000/ask_gpt', json=dictToSend)
print('response from server:',res.text)
dictFromServer = res.json()