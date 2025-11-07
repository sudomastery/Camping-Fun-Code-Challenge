from flask import Blueprint, request, jsonify
from src.models.signup import Signup
from src.schemas.signup import SignupSchema
from src.extensions import db

signups_bp = Blueprint('signups', __name__)
signup_schema = SignupSchema()
signups_schema = SignupSchema(many=True)

@signups_bp.route('/signups', methods=['POST'])
def create_signup():
    data = request.get_json()
    try:
        signup = signup_schema.load(data)
        db.session.add(signup)
        db.session.commit()
        return signup_schema.jsonify(signup), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@signups_bp.route('/signups', methods=['GET'])
def get_signups():
    signups = Signup.query.all()
    return signups_schema.jsonify(signups), 200

@signups_bp.route('/signups/<int:signup_id>', methods=['GET'])
def get_signup(signup_id):
    signup = Signup.query.get_or_404(signup_id)
    return signup_schema.jsonify(signup), 200

@signups_bp.route('/signups/<int:signup_id>', methods=['PUT'])
def update_signup(signup_id):
    data = request.get_json()
    signup = Signup.query.get_or_404(signup_id)
    try:
        signup = signup_schema.load(data, instance=signup)
        db.session.commit()
        return signup_schema.jsonify(signup), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@signups_bp.route('/signups/<int:signup_id>', methods=['DELETE'])
def delete_signup(signup_id):
    signup = Signup.query.get_or_404(signup_id)
    db.session.delete(signup)
    db.session.commit()
    return jsonify({"message": "Signup deleted"}), 204