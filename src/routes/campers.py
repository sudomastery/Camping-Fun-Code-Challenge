from flask import Blueprint, request, jsonify
from ..controllers.campers_controller import CampersController

campers_bp = Blueprint('campers', __name__)

@campers_bp.route('/campers', methods=['GET'])
def get_campers():
    return CampersController.get_all_campers()

@campers_bp.route('/campers', methods=['POST'])
def create_camper():
    data = request.get_json()
    return CampersController.create_camper(data)

@campers_bp.route('/campers/<int:camper_id>', methods=['GET'])
def get_camper(camper_id):
    return CampersController.get_camper(camper_id)

@campers_bp.route('/campers/<int:camper_id>', methods=['PUT'])
def update_camper(camper_id):
    data = request.get_json()
    return CampersController.update_camper(camper_id, data)

@campers_bp.route('/campers/<int:camper_id>', methods=['DELETE'])
def delete_camper(camper_id):
    return CampersController.delete_camper(camper_id)