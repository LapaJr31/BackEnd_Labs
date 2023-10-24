from flask import Blueprint

healthy = Blueprint('healthy', __name__)

@healthy.route("/healthy")
def health_check():
    return "Healthy"
