from flask import Blueprint, jsonify, request
from extensions import db
from models.activity import Activity

activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return jsonify([a.to_dict_basic() for a in activities]), 200

@activities_bp.route('/activities', methods=['POST'])
def create_activity():
    """Create a new activity. Expects JSON {"name": str, "difficulty": int}."""
    data = request.get_json() or {}
    try:
        activity = Activity(name=data.get("name"), difficulty=data.get("difficulty"))
        db.session.add(activity)
        db.session.commit()
        return jsonify(activity.to_dict_basic()), 201
    except Exception:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400

@activities_bp.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    activity = Activity.query.get(activity_id)
    if not activity:
        return jsonify({"error": "Activity not found"}), 404
    db.session.delete(activity)  # cascades signups
    db.session.commit()
    return '', 204