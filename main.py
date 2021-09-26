import numpy as np
from flask import Flask, render_template, jsonify, request
import joblib
import pickle
import pandas as pd
import sklearn
#from flask_mysql_connector import MySQL
#from flask import MySQL
#import yaml
#import ML model


app = Flask(__name__)

#Config Database
#db = yaml.load(open('database.yaml'))
#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_DB'] = db['mysql_db']

#mysql = MySQL(app)

#model = pickle.load(open('car_price_prediction_xgboost.pickle', 'rb'))
#model = joblib.load("car_price_prediction.joblib.dat")
model_file = open("car_price_prediction_linear_regression.pickle",'rb')
model = pickle.load(model_file)

#set default route
@app.route('/', methods=['GET'])
def home():
    return render_template(
        'custom_index.html'
    )


@app.route('/predict', methods=['POST', 'GET'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_feature = [np.array(int_features)]
    prediction = model.predict(final_feature)

    # round last 2 digit behind .
    result = round(prediction[0], 2)
    #set a condition
    #if the result is greater than 0
    if result < 0:
        return render_template('custom_index.html', prediction_text='BOOM')
    # if the result is less than 0
    else:
        return render_template('custom_index.html', prediction_text='Car Price Prediction $ {}'.format(result))


#let it display debugging
if __name__ == "__main__":
    app.run(debug=True)

