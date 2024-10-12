import openai
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import apis

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    client = apis.get_apis(api="open_ai")
    client.test_prompt()
    return "¡Hola, Flask!"


@app.route("/query-gpt", methods=["POST"])
def query_gpt():
    data = request.get_json()
    try:
        prompt = data["prompt"]
        client = apis.get_apis(api="open_ai")
        response = client.custom_prompt(prompt=prompt)
        response_dd = {
            'message': "Datos recibidos correctamente",
            'response': response
        }
        status = 200
    except Exception as exc:
        print("exception found", exc)
        response_dd = {
            "message": "Ocurrió un error, comunique al administrador.",
            "response": "error",
        }
        status = 400
    return jsonify(response_dd), status

if __name__ == "__main__":
    app.run(debug=True, port=5001)