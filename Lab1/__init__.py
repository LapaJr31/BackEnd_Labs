from flask import Flask
import healthCheck

app = Flask(__name__)

app.register_blueprint(healthCheck.healthy)

@app.route("/")
def hello():
    return "Hello World!"


