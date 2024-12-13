from extensions import mysql
from models import PreferenceGroup

class PreferenceGroupService:
    # Variable para guardar las respuestas
    _preference_responses = {}

    @staticmethod
    # Metodo para obtener todas las preguntas de preference
    def get_all_questions():
        try:
            with mysql.connection.cursor() as cursor:  # Usar "with" para liberar automáticamente el cursor
                cursor.execute("SELECT id_preference_group, `group`, question FROM preference_group")
                rows = cursor.fetchall()
            return [PreferenceGroup(*row).serialize() for row in rows]
        except Exception as e:
            # Manejo de errores para evitar que falle silenciosamente
            print(f"Error obteniendo preguntas de preference_group: {e}")
            return []

    @staticmethod
    # Metodo para guardar las respuestas de las preguntas de preference
    def save_responses(responses):
        print("Respuestas de preferencias:", responses)
        try:
            if not isinstance(responses, dict): #Validar que sea un diccionario
                raise ValueError("El formato de las respuestas no es valido")
            # Guardar las respuestas en la variable
            PreferenceGroupService._preference_responses = responses
            return {"message": "Respuesta guardadas correctamente"}
        except Exception as e:
            print(f"Error guardando preguntas de preference: {e}")
            return {"message": "Ocurrió un error al guardar las respuestas.", "error": str(e)}

    @staticmethod
    # Metodo para obtener las respuestas almacenadas
    def get_saved_responses():
        return PreferenceGroupService._preference_responses