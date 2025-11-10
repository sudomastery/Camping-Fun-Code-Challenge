from flask import Blueprint, request, jsonify
from ..models.camper import Camper
from ..schemas.camper import CamperSchema
from ..extensions import db

campers_bp = Blueprint('campers', __name__)

@campers_bp.route('/campers', methods=['POST'])
def create_camper():
    data = request.get_json()
    camper_schema = CamperSchema()
    camper = camper_schema.load(data)
    db.session.add(camper)
    db.session.commit()
    return camper_schema.dump(camper), 201

@campers_bp.route('/campers', methods=['GET'])
def get_campers():
    campers = Camper.query.all()
    camper_schema = CamperSchema(many=True)
    return camper_schema.dump(campers), 200

@campers_bp.route('/campers/<int:camper_id>', methods=['GET'])
def get_camper(camper_id):
    camper = Camper.query.get_or_404(camper_id)
    camper_schema = CamperSchema()
    return camper_schema.dump(camper), 200

@campers_bp.route('/campers/<int:camper_id>', methods=['PUT'])
def update_camper(camper_id):
    camper = Camper.query.get_or_404(camper_id)
    data = request.get_json()
    camper_schema = CamperSchema()
    camper = camper_schema.load(data, instance=camper)
    db.session.commit()
    return camper_schema.dump(camper), 200

@campers_bp.route('/campers/<int:camper_id>', methods=['DELETE'])
def delete_camper(camper_id):
    camper = Camper.query.get_or_404(camper_id)
    db.session.delete(camper)
    db.session.commit()
    return '', 204