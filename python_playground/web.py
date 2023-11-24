from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# FLASK_APP=python_playground.web flask run --host=0.0.0.0 --port=8001


@app.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name: str) -> str:
    return f"Hello, {escape(name)}!"
