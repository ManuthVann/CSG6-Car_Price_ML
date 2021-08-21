import numpy as np
from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import sklearn
#import ML model
app = Flask(__name__)
model = pickle.load(open('loan_amount_prediction_easymoney.pickle', 'rb'))
#set default route
@app.route('/', methods=['GET'])
def home():
    return render_template(
        'custom_index.html'
    )
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_feature = [np.array(int_features)]
    prediction = model.predict(final_feature)
    # round last 2 digit behind .
    result = round(prediction[0], 2)
    #set a condition
    #if the result is greater than 0
    if result < 0:
        return render_template('custom_index.html', prediction_text='Requester is NOT approved')
    # if the result is less than 0
    else:
        return render_template('custom_index.html', prediction_text='Loan $ For Request-er $ {}'.format(result))
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.route('/predict_api', methods=["GET","POST"])
def predict_api():
    #data = request.get_json(force=True)
    data = request.json
    query_df = pd.DataFrame(data)
    prediction = model.predict(query_df)
    # return flask.jsonify(**result)
    return jsonify({"Loan $ Prediction Results: ": list(prediction)})

@app.route('/request_json', methods=["GET"])
def request_json():
    data = request.get_json()

    installment = data['installment']
    term = data['term']
    borrower_month_income = data['borrower_month_income']
    borrower_length_experience = data['borrower_length_experience']
    home_ownership = data['home_ownership']
    address_state = data['address_state']

    prediction = model.predict(installment, term, borrower_month_income
                               ,borrower_length_experience,home_ownership,
                               address_state)
    return jsonify({"Loan $ Prediction Results": prediction})

#let it display debugging
if __name__ == "__main__":
    app.run(debug=True)
