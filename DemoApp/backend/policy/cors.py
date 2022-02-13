from flask_cors import CORS
from flask import make_response

#CORS permissions
def fix_cors(app):
    CORS(app)
    cors = CORS(app, resources={
        r"/*": {
            "origins": "*"
        }
    })
    return cors

def create_response(responseBody, responseType='text/json'):
    res = make_response(responseBody)
    res.headers['Content-Type'] = responseType
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    res.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, Token"
    return res