from flask import request, jsonify
from flask import json


url = 'http://localhost:5000/predict_api'


r = request.post(url, json={
    'installment':200,
    'term':36,
    'borrower_length_experience':3,
    'home_ownership':3,
    'borrower_month_income':500,
    'address_state':1
})
print(r.json())
