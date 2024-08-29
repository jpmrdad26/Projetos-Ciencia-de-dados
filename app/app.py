import pickle

import numpy as np
from flask import Flask, request, jsonify
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from

app = Flask(__name__)
# Embora nao seja uma boa ideia usar links relativos, como é uma POC, é ok
model = pickle.load(open("..\\ml\\trained-model\\model.pkl", "rb"))

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
    data = {}  # dictionary to store result
    data['code'] = 1
    data_n = request.get_json()
    try:
        array = np.array(data_n["array"])

    # for invalid data keys
    except KeyError:
        return jsonify({"responseCode": "2", "responseDesc": "Invalid data Key"}), 400

    # if the input is empty
    if array is None:
        print("Array Input Failed..")
        data['response'] = 'Input Reading Error: Input is Empty'
        return jsonify({"responseCode": "3", "responseDesc": "Input Reading Error: Input is Empty"}), 400

    # if the input array is not the required size
    elif len(array) != 11:
        print("Array Input InComplete..")
        data['response'] = 'Input Reading Error: Input is Incomplete'
        return jsonify({"responseCode": "3", "responseDesc": "Input Reading Error: Input is Incomplete"}), 400

    else:
        array = array.reshape(1, 11)
        # prediction
        prediction = model.predict(array)
        data['code'] = 0
        data['response'] = 'Model prediction PASSED'
        data['prediction'] = prediction
        response = {"responseCode": "0", "responseDesc": "SUCCESS", "Wine Quality": prediction[0]}
        return jsonify(response), 200


if __name__ == "__main__":
    app.run()
