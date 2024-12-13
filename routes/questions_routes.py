from flask import Blueprint, jsonify, request
from services.questions_service import QuestionsService

questions_bp = Blueprint('questions_bp', __name__)

@questions_bp.route('/intelligences/questions', methods=['GET'])
def get_intelligence_questions():
    questions = QuestionsService.get_all_questions()
    if questions:
        return jsonify(questions)
    else:
        return jsonify({"message": "No se encontraron preguntas o ocurrió un error"}), 404  # Not Found

@questions_bp.route('/intelligences/responses', methods=['POST'])
def save_intelligence_responses():
    try:
        responses = request.json  # Obtener datos JSON del cuerpo de la solicitud
        if not responses:
            return jsonify({"message": "El cuerpo de la solicitud está vacío."}), 400

        result = QuestionsService.save_responses(responses)
        return jsonify(result), 200 if "error" not in result else 500
    except Exception as e:
        return jsonify({"message": "Error procesando la solicitud.", "error": str(e)}), 500