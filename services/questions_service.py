from extensions import mysql
from models import Questions

class QuestionsService:
    # Variable para guardar las respuestas
    _intelligence_responses = {}

    @staticmethod
    # Metodo para obtener todas las preguntas de questions (intelligence)
    def get_all_questions():
        try:
            with mysql.connection.cursor() as cursor:  # Usar "with" para liberar automáticamente el cursor
                cursor.execute("SELECT id_questions, id_intelligences, `questions`, order_number FROM questions")
                rows = cursor.fetchall()
            return [Questions(*row).serialize() for row in rows]
        except Exception as e:
            # Manejo de errores para evitar que falle silenciosamente
            print(f"Error obteniendo preguntas de questions (intelligence): {e}")
            return []

    @staticmethod
    # Metodo para guardar las respuestas
    def save_responses(responses):
        print("Respuestas de inteligencia:", responses)
        try:
            if not isinstance(responses, dict):  # Validar que sea un diccionario
                raise ValueError("El formato de las respuestas no es válido.")
            # Validación adicional: verificar que cada clave tenga una lista como valor
            for key, value in responses.items():
                if not isinstance(value, list) or not all(isinstance(v, bool) for v in value):
                    raise ValueError(f"El formato de las respuestas para '{key}' no es válido. Deben ser listas de booleanos.")
            # Guardar las respuestas en memoria
            QuestionsService._intelligence_responses = responses
            return {"message": "Respuestas de inteligencias guardadas correctamente."}
        except Exception as e:
            print(f"Error guardando respuestas de inteligencia: {e}")
            return {"message": "Ocurrió un error al guardar las respuestas.", "error": str(e)}

    @staticmethod
    # Metodo para obtener las respuestas almacenadas
    def get_intelligence_responses():
        return QuestionsService._intelligence_responses