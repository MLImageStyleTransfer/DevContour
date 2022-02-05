from flask import Flask
from dotenv import dotenv_values


def make_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5555


app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug=True, port=make_port())