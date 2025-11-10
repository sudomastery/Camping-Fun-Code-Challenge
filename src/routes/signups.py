from flask import Blueprint, request, jsonify
from src.controllers.signups_controller import SignupsController

signups_bp = Blueprint('signups', __name__)

@signups_bp.route('/signups', methods=['POST'])
def create_signup():
    data = request.get_json()
    return SignupsController.create_signup(data)

@signups_bp.route('/signups/<int:signup_id>', methods=['GET'])
def get_signup(signup_id):
    return SignupsController.get_signup(signup_id)

@signups_bp.route('/signups/<int:signup_id>', methods=['PUT'])
def update_signup(signup_id):
    data = request.get_json()
    return SignupsController.update_signup(signup_id, data)

@signups_bp.route('/signups/<int:signup_id>', methods=['DELETE'])
def delete_signup(signup_id):
    return SignupsController.delete_signup(signup_id)