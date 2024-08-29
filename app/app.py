import pickle

import numpy as np
from flask import Flask
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("C:\\Users\\ramos\\GT\\Projetos-Ciencia-de-dados\\model.pkl", "rb"))


@app.route('/')
def home():
    final_features = np.array(
        [[-1.72, -1.41, 0.47, 1.30, 0.48, -1.17, -0.38, -1.31, -2.05, -2.09, -0.31, -0.61, -0.54, -1.43, -1.89]])

    resultado = model.predict(final_features)

    return {
        "min": resultado.min,
        max: resultado.max
    }


if __name__ == "__main__":
    app.run()
