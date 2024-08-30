import pickle
from wsgiref.simple_server import WSGIServer

import numpy as np
from flasgger import Swagger, swag_from
from flask import Flask, request, jsonify

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Expectativa de Vida - Previsão",
        "description": "Api para previão da expectativa de vida",
        "contact": {
            "name": "Joao Pedro",
            "email": "c00011310@cassi.com.br",
        },
        "version": "1.0",
        "basePath": "http://localhost:5000",
    },
    "schemes": [
        "http",
        "https"
    ],
}

swagger_config = {
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST"),
    ],
    "specs": [
        {
            "endpoint": 'Open Api Doc',
            "route": '/openapi_api_doc.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/",

}
swagger = Swagger(app, template=swagger_template, config=swagger_config)


@swag_from("docs/predict.yaml")
@app.route("/predict", methods=["POST"])
def predict():
    data_n = request.get_json()
    try:
        array = np.array(data_n["data"])
    except KeyError:
        return jsonify({
            "data": None,
            "mensagens": ["Não foi possível validar este array"]
        }), 400

    if array is None:
        return jsonify({
            "data": None,
            "mensagens": ["data é obrigatório"]
        }), 400

    # if the input array is not the required size
    elif len(array) != 15:
        return jsonify({
            "data": None,
            "mensagens": ["data deve ter 15 posições, conforme documentação"]
        }), 400

    else:
        array = array.reshape(1, 15)
        prediction = model.predict(array)
        response = {"data": {
            "previsao": prediction[0]
        }}
        return jsonify(response), 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
