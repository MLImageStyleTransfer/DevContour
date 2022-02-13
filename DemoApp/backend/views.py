from flask import request
from flask import make_response
from flask import jsonify

from runner import app, make_port
from controllers.black_white import grayscale_transform

# from policy.cors import create_response
from flask_cors import cross_origin

@app.route('/')
@cross_origin()
def index():
    open_tag = '<h1 width="100%" align="center">'
    close_tag = '</h1>'

    content = 'Backend demo feature-service!'
    port = 'Started on port: ' + str(make_port())
    br = '<br/>'

    simple_render = [open_tag, content, br, port, close_tag]

    return ' '.join(simple_render)

# def create_response(responseBody, responseType='text/json'):
#     res = make_response(responseBody)
#     res.headers['Content-Type'] = responseType
#     res.headers["Access-Control-Allow-Origin"] = "*"
#     res.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
#     res.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, Token"
#     return res

@app.route('/api/grayscale/', methods=['POST'])
@cross_origin()
def black_white_transform(xxx):
#     request.headers['Content-Type'] = 'text/json'
#     request.headers["Access-Control-Allow-Origin"] = "*"
#     request.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
#     request.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, Token"
#     print(request.json())
#     return create_response(
#         jsonify({'file': grayscale_transform(request.files['file'].stream)})
#     )
#     response = jsonify(message="Simple server is running")

    # Enable Access-Control-Allow-Origin
#     response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:3000")
#     response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:3000"
#     return response
    return jsonify('AAAAAAs\t' + str(xxx))
