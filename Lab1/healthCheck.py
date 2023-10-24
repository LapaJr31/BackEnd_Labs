from flask import Blueprint,jsonify

healthy = Blueprint('healthy', __name__)

@healthy.route("/healthy")
def health_check():
    response = {
        'status': 'healthy'
    }
    return jsonify(response), 200
