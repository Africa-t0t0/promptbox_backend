import openai
import os

from flask import Flask

from utils import apis

app = Flask(__name__)

@app.route('/')
def home():
    client = apis.get_apis(api="open_ai")
    client.test_prompt()
    return "¡Hola, Flask!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)