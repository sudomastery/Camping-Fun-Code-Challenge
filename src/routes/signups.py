from flask import Blueprint, jsonify, request
from extensions import db
from models.signup import Signup
from models.camper import Camper
from models.activity import Activity

signups_bp = Blueprint('signups', __name__)

@signups_bp.route('/signups', methods=['POST'])
def create_signup():
    data = request.get_json() or {}
    try:
        camper_id = data.get("camper_id")
        activity_id = data.get("activity_id")
        time = data.get("time")

        # Must reference existing records
        if Camper.query.get(camper_id) is None or Activity.query.get(activity_id) is None:
            return jsonify({"errors": ["validation errors"]}), 400

        signup = Signup(camper_id=camper_id, activity_id=activity_id, time=time)
        db.session.add(signup)
        db.session.commit()
        return jsonify(signup.to_dict_full()), 201
    except Exception:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400