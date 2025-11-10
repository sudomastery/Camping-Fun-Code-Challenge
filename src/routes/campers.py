# FILE: src/routes/campers.py
from flask import Blueprint, jsonify, request
from extensions import db
from models.camper import Camper

campers_bp = Blueprint('campers', __name__)

@campers_bp.route('/campers', methods=['GET'])
def get_campers():
    campers = Camper.query.all()
    return jsonify([c.to_dict_basic() for c in campers]), 200

@campers_bp.route('/campers/<int:camper_id>', methods=['GET'])
def get_camper(camper_id):
    camper = Camper.query.get(camper_id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404
    data = {
        "id": camper.id,
        "name": camper.name,
        "age": camper.age,
        "signups": [s.to_dict_with_activity() for s in camper.signups],
    }
    return jsonify(data), 200



# FILE: src/routes/campers.py
@campers_bp.route('/campers', methods=['POST'])
def create_camper():
    data = request.get_json() or {}
    try:
        camper = Camper(name=data.get("name"), age=data.get("age"))
        db.session.add(camper)
        db.session.commit()
        return jsonify(camper.to_dict_basic()), 201
    except Exception:
        db.session.rollback()
        # Spec requires generic message
        return jsonify({"errors": ["validation errors"]}), 400
    

# FILE: src/routes/campers.py
@campers_bp.route('/campers/<int:camper_id>', methods=['PATCH'])
def update_camper(camper_id):
    camper = Camper.query.get(camper_id)
    if not camper:
        return jsonify({"error": "Camper not found"}), 404

    data = request.get_json() or {}
    try:
        if "name" in data:
            camper.name = data["name"]
        if "age" in data:
            camper.age = data["age"]
        db.session.commit()
        return jsonify(camper.to_dict_basic()), 202  # Spec uses 202
    except Exception:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400