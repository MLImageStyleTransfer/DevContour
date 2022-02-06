from runner import app, make_port
import controllers.black_white as func


@app.route('/')
def index():
    open_tag = '<h1 width="100%" align="center">'
    close_tag = '</h1>'

    content = 'Backend demo feature-service!'
    port = 'Started on port: ' + str(make_port())
    br = '<br/>'

    simple_render = [open_tag, content, br, port, close_tag]

    return ' '.join(simple_render)


@app.route('/black-white/', methods=["GET"])
def black_white_transform():
    return func.black_white_transform()
