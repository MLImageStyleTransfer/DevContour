from flask import request
from flask import make_response
from flask import jsonify

from runner import app, make_port
from controllers.black_white import grayscale_transform


@app.route('/')
def index():
    open_tag = '<h1 width="100%" align="center">'
    close_tag = '</h1>'

    content = 'Backend demo feature-service!'
    port = 'Started on port: ' + str(make_port())
    br = '<br/>'

    simple_render = [open_tag, content, br, port, close_tag]
    return ' '.join(simple_render)


@app.route('/api/grayscale/', methods=['POST'])
def black_white_transform():
    value = str(request.data)[3:-2]
    res_file = str(grayscale_transform(value))
    response = jsonify(res_file)

    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    return response
