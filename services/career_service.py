from models import Career
from extensions import mysql

class CareerService:

    @staticmethod
    # Metodo para obtener las carreras a traves del id_branch
    def get_career_branch_id(id_branch):
        try:
            with mysql.connection.cursor() as cursor:
                query = """SELECT id_career, name, title_intermediate, description, duration_months, id_type_career, id_modality, id_branch,id_range FROM career WHERE id_branch = %s"""
                cursor.execute(query, (id_branch,))
                rows = cursor.fetchall()
                careers = [Career(*row).serialize() for row in rows]
                return careers
        except Exception as e:
            print(f"Error obteniendo carreras de career por id_branch: {e}")
            return []

    @staticmethod
    # Metodo para buscar carreras por nombre y con filtros
    def get_career_by_name(name, title_intermediate=None, duration_months=None, id_type_career=None, id_modality=None, id_branch=None, id_range=None):
        try:
            query = """SELECT id_career, name, title_intermediate, description, duration_months, id_type_career, id_modality, id_branch,id_range FROM career WHERE name LIKE %s"""
            params = (f"%{name}%",)
            if title_intermediate is not None:
                query += """ AND title_intermediate = %s"""
                params += (title_intermediate,)
            if duration_months is not None:
                query += """ AND duration_months = %s"""
                params += (duration_months,)
            if id_type_career is not None:
                query += """ AND id_type_career = %s"""
                params += (id_type_career,)
            if id_modality is not None:
                query += """ AND id_modality = %s"""
                params += (id_modality,)
            if id_branch is not None:
                query += """ AND id_branch = %s"""
                params += (id_branch,)
            if id_range is not None:
                query += """ AND id_range = %s"""
                params += (id_range,)
            with mysql.connection.cursor() as cursor:
                cursor.execute(query, params)
                rows = cursor.fetchall()
                careers = [Career(*row).serialize() for row in rows]
                return careers
        except Exception as e:
            print(f"Error buscando carreras: {e}")
            return []