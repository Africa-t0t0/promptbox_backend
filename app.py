import openai
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import apis
from utils import utils

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
        language = utils.detect_language(text=response)
        response_dd = {
            "message": "Datos recibidos correctamente",
            "response": response,
            "language": language
        }
        print("resp", response)
        status = 200
    except Exception as exc:
        print("exception found", exc)
        response_dd = {
            "message": "Ocurrió un error, comunique al administrador.",
            "response": "error",
        }
        status = 400
    return jsonify(response_dd), status


@app.route("/dummy", methods=["GET"])
def dummy():
    text = "Aquí tienes un ejemplo de código en Python que lee un archivo CSV y lo convierte en un archivo PDF utilizando la librería pandas y matplotlib: ```python import pandas as pd import matplotlib.pyplot as plt # Leer el archivo CSV df = pd.read_csv('archivo.csv') # Crear visualización de los datos plt.figure(figsize=(10, 6)) plt.table(cellText=df.values, colLabels=df.columns, loc='center') plt.axis('off') plt.savefig('output.pdf') plt.close() ``` Este código lee un archivo CSV llamado 'archivo.csv', crea una visualización de los datos en forma de tabla y guarda esta visualización como un archivo PDF llamado 'output.pdf'. Recuerda que necesitarás instalar las librerías pandas y matplotlib para poder ejecutar este código."
    response_dd = {
        "message": "success",
        "response": text
    }
    return jsonify(response_dd), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)