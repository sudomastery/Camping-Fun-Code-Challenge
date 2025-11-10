# FILE: src/routes/campers.py
from flask import Blueprint, jsonify, request
from extensions import db
from models.camper import Camper

campers_bp = Blueprint('campers', __name__)

@campers_bp.route('/campers', methods=['GET'])
def get_campers():
    campers = Camper.query.all()
    return jsonify([c.to_dict_basic() for c in campers]), 200