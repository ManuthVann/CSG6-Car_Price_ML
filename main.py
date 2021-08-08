import numpy as np
from flask import Flask, render_template, jsonify, request
import pickle
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
#Not Worked yet
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    result = prediction[0]
    return jsonify(result)
#let it display debugging
if __name__ == "__main__":
    app.run(debug=True)
