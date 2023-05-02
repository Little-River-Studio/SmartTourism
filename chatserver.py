from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import os
from _data import chat

app = Flask(__name__)
CORS(app)

openai.api_key = "KEY"

@app.route('/', methods=['POST'])
def openai_chat():

    data = request.json
    message = data['message']
    ID = data['ID']

    role = "你是一个泰山" + chat[ID] + "的导游"
    messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": message},
        ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    text = response['choices'][0]['message']['content']
    return jsonify({'response': text.replace('\n\n', '\n')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
