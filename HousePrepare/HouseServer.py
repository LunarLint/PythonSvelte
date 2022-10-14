from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello World"


@app.route("/predict", methods=["POST"])
def predict():
    feature_dict = request.get_json()
    X = pd.DataFrame.from_dict(feature_dict)
    prediction = clf.predict(X)
    return jsonify({"prediction":
                   round(float(prediction), 1)})


if __name__ == '__main__':
    clf = joblib.load("HouseModel.pkl")
    app.run(debug=True)
