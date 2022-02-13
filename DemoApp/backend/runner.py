from flask import Flask
from dotenv import dotenv_values
from policy.cors import fix_cors
from flask_cors import CORS


def make_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5555


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

from views import *

if __name__ == "__main__":
#     fix_cors(app)
    app.run(debug=True, port=make_port())