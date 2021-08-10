from flask import request, jsonify
from flask import json


url = 'http://localhost:5000/predict_api'


r = request.post(url, json={
    'installment':'borrower_length_experience',
    'term':'term',
    'borrower_length_experience':'borrower_length_experience',
    'home_ownership':'home_ownership',
    'borrower_month_income':'borrower_month_income',
    'address_state':'address_state'
})
print(r.json())
