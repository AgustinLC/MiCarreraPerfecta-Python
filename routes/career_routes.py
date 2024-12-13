from flask import Blueprint, jsonify, request
from services.career_service import CareerService

career_bp = Blueprint('career', __name__)

@career_bp.route('/career/branch', methods=['GET'])
def get_career_branch_id():
    data = request.get_json()
    id_branch = data.get('id_branch')
    career = CareerService.get_career_branch_id(id_branch)
    if career:
        return jsonify(career), 200
    else:
        return jsonify({"message": "No se encontraron las carreras con el id_branch"}), 404

@career_bp.route('/career/search', methods=['GET'])
def get_career_search():
    data = request.get_json()
    name = data.get('name')
    title_intermediate = data.get('title_intermediate')
    duration_months = data.get('duration_months')
    id_type_career = data.get('id_type_career')
    id_modality = data.get('id_modality')
    id_branch = data.get('id_branch')
    id_range = data.get('id_range')
    career = CareerService.get_career_by_name(name, title_intermediate, duration_months, id_type_career, id_modality, id_branch, id_range)
    if career:
        return jsonify(career), 200
    else:
        return jsonify({"message": "No se encontraron las carreras"})