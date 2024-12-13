from flask import Blueprint, jsonify
from services.branch_service import BranchService

branch_bp = Blueprint('branch_bp', __name__)

@branch_bp.route('/branch/top', methods=['GET'])
def get_branch_routes():
    branch = BranchService.get_top_three_branch()
    if branch:
        return jsonify(branch), 200
    else:
        return jsonify({"message": "No se encontraron el top tres de ramas o ocurrió un error"}), 404