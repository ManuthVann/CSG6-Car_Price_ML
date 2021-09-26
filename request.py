from flask import request, jsonify
from flask import json
url = 'http://localhost:5000/predict'
r = request.post(url, json={
    "year": "year",
    "manufacturer": "manufacturer",
    "cylinder": "cylinder",
    "model": "model",
    "fuel": "fuel",
    "kms_driven": "kms_driven",
    "status":"status",
    "transmission":"transmission",
    "drive_wheel":"drive_wheel",
    "body_type":"body_type",
    "colour":"colour"
})