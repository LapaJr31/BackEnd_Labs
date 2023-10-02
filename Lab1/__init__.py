from flask import Flask
from health_check import healthy

app = Flask(__name__)

app.register_blueprint(healthy)

@app.route("/")
def hello():
    return "Hello World!"
