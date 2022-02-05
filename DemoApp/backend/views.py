from runner import app
import controllers.black_white as func


@app.route("/black-white")
def black_white_transform():
    return func.black_white_transform()