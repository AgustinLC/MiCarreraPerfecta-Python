from flask import Blueprint, jsonify, request
from services.preference_group_service import PreferenceGroupService

preference_bp = Blueprint('preference_bp', __name__)

@preference_bp.route('/preferences/questions', methods=['GET'])
def get_preference_questions():
    preference_group = PreferenceGroupService.get_all_questions()
    if preference_group:
        return jsonify(preference_group), 200  # OK
    else:
        return jsonify({"message": "No se encontraron preguntas o ocurrió un error"}), 404  # Not Found

@preference_bp.route('/preferences/responses', methods=['POST'])
def save_preference_responses():
    try:
        responses = request.json #Obetiene los datos del cuerpo de la solicitud
        if not responses:
            return jsonify({"message": "El cuerpo de la solicitud esta vacio"}), 400
        result = PreferenceGroupService.save_responses(responses)
        return jsonify(result), 200 if "error" not in result else 500
    except Exception as e:
        return jsonify({"message": "Error procesando la solicitud.", "error": str(e)}), 500