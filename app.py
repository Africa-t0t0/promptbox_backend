from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import apis, decorators, handlers, utils

app = Flask(__name__)
CORS(app)


@app.route("/query-gpt", methods=["POST"])
@decorators.validate_token
def query_gpt():
    data_dd = request.get_json()
    try:
        prompt = data_dd["prompt"]
        client = apis.get_apis(api="open_ai")
        response = client.custom_prompt(prompt=prompt)
        language = utils.detect_language(text=response)
        response_dd = {
            "message": "Datos recibidos correctamente",
            "response": response,
            "language": language
        }
        status = 200
    except Exception as exc:
        response_dd = {
            "message": f"Error: {exc}",
            "response": "error",
        }
        status = 400
    return jsonify(response_dd), status


@app.route("/dummy", methods=["GET"])
@decorators.validate_token
def dummy():
    text = "Aquí tienes un ejemplo de código en Python que lee un archivo CSV y lo convierte en un archivo PDF utilizando la librería pandas y matplotlib: ```python import pandas as pd import matplotlib.pyplot as plt # Leer el archivo CSV df = pd.read_csv('archivo.csv') # Crear visualización de los datos plt.figure(figsize=(10, 6)) plt.table(cellText=df.values, colLabels=df.columns, loc='center') plt.axis('off') plt.savefig('output.pdf') plt.close() ``` Este código lee un archivo CSV llamado 'archivo.csv', crea una visualización de los datos en forma de tabla y guarda esta visualización como un archivo PDF llamado 'output.pdf'. Recuerda que necesitarás instalar las librerías pandas y matplotlib para poder ejecutar este código."
    response_dd = {
        "message": "success",
        "response": text
    }
    return jsonify(response_dd), 200


if __name__ == "__main__":
    cleaned_dd = handlers.handle_server_configuration()

    debug = cleaned_dd["debug"]
    port = cleaned_dd["port"]

    app.run(debug=debug, port=port)
