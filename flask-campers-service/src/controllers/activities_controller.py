from flask import Blueprint, request, jsonify
from src.models.activity import Activity
from src.schemas.activity import ActivitySchema
from src.extensions import db

activities_bp = Blueprint('activities', __name__)
activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)

@activities_bp.route('/activities', methods=['POST'])
def create_activity():
    json_data = request.get_json()
    activity = activity_schema.load(json_data)
    db.session.add(activity)
    db.session.commit()
    return activity_schema.jsonify(activity), 201

@activities_bp.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return activities_schema.jsonify(activities), 200

@activities_bp.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    return activity_schema.jsonify(activity), 200

@activities_bp.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    json_data = request.get_json()
    activity = Activity.query.get_or_404(activity_id)
    activity_schema.load(json_data, instance=activity, partial=True)
    db.session.commit()
    return activity_schema.jsonify(activity), 200

@activities_bp.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    db.session.delete(activity)
    db.session.commit()
    return '', 204