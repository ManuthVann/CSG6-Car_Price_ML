#import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model_file = open("car_price_prediction_linear_regression.pickle", 'rb')
best_model = pickle.load(model_file)

#model = pickle.load(open('car_price_prediction_xgboost.pickle', 'rb'))


@app.route('/')
def home():
    return "<h1> Car price prediction is starting </h1>"


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = best_model.predict(query_df)

    return jsonify({"result": list(prediction)})


if __name__ == "__main__":
    app.run(debug=True)
