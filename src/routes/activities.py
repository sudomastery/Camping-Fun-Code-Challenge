from flask import Blueprint, request, jsonify
from ..controllers.activities_controller import ActivitiesController

activities_bp = Blueprint('activities', __name__)
controller = ActivitiesController()

@activities_bp.route('/activities', methods=['GET'])
def get_activities():
    return jsonify(controller.get_all_activities()), 200

@activities_bp.route('/activities', methods=['POST'])
def create_activity():
    data = request.get_json()
    return jsonify(controller.create_activity(data)), 201

@activities_bp.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    return jsonify(controller.get_activity(activity_id)), 200

@activities_bp.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    data = request.get_json()
    return jsonify(controller.update_activity(activity_id, data)), 200

@activities_bp.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    return jsonify(controller.delete_activity(activity_id)), 204