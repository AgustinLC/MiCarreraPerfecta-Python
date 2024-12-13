from flask import Blueprint, jsonify
from extensions import mysql

example_bp = Blueprint('example_bp', __name__)

@example_bp.route('/test-db', methods=['GET'])
def test_db():
    try:
        # Usar el cursor para ejecutar consultas
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT DATABASE();')
        db_name = cursor.fetchone()
        cursor.close()
        return jsonify({"message": f"Conexion exitosa a la base de datos: {db_name[0]}"})
    except Exception as e:
        return jsonify({"message": str(e)})
