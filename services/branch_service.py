from collections import Counter
from extensions import mysql
from models import Branch
from services.preference_group_service import PreferenceGroupService
from services.questions_service import QuestionsService

class BranchService:

    @staticmethod
    def get_branch_ids_from_preference_groups():
        preference_responses = PreferenceGroupService.get_saved_responses()
        preference_group_ids = []
        if preference_responses:
            mapping = {
                "cognitiva": 1,
                "social": 2,
                "motor": 3,
                "creativo": 4,
                "emocional": 5,
                "linguistico": 6,
                "tecnologico": 7,
                "resolutivo": 8,
                "adaptativo": 9,
                "eticoymoral": 10
                }
            for key, group_id in mapping.items():
                if preference_responses.get(key):
                    preference_group_ids.append(group_id)
            if not preference_group_ids:
                return []

        try:
            with mysql.connection.cursor() as cursor:
                # Obtener IDs de preferencias
                query = """SELECT DISTINCT id_preference FROM preference WHERE id_preference_group IN (%s)"""
                format_strings = ",".join(["%s"] * len(preference_group_ids))
                cursor.execute(query % format_strings, tuple(preference_group_ids))
                preference_ids = [row[0] for row in cursor.fetchall()]
                if not preference_ids:
                    return []
                # Obtener IDs de WordKey
                query = """SELECT DISTINCT id_word_key FROM preference_words_key WHERE id_preference IN (%s)"""
                format_strings = ",".join(["%s"] * len(preference_ids))
                cursor.execute(query % format_strings, tuple(preference_ids))
                word_key_ids = [row[0] for row in cursor.fetchall()]
                if not word_key_ids:
                    return []
                # Obtener IDs de ramas
                query = """SELECT DISTINCT id_branch FROM branch_words_key WHERE id_word_key IN (%s)"""
                format_strings = ",".join(["%s"] * len(word_key_ids))
                cursor.execute(query % format_strings, tuple(word_key_ids))
                branch_ids = [row[0] for row in cursor.fetchall()]
                return branch_ids
        except Exception as e:
            print(f"Error obteniendo branches de preferences: {e}")
            return []

    @staticmethod
    def get_all_branch_for_intelligence():
        intelligence_responses = QuestionsService.get_intelligence_responses()
        intelligence_mapping = {
            "espacial": 1,
            "corporal": 2,
            "naturalista": 3,
            "musical": 4,
            "linguistica": 5,
            "intrapersonal": 6,
            "matematica": 7,
            "interpersonal": 8
        }
        qualifying_intelligences = [intelligence_mapping[key] for key, responses in intelligence_responses.items() if responses.count(True) >= 5]
        if not qualifying_intelligences:
            return []
        try:
            with mysql.connection.cursor() as cursor:
                query = """SELECT DISTINCT id_branch FROM branch_intelligence WHERE id_intelligence IN (%s) AND priority = 1"""
                format_strings = ",".join(["%s"] * len(qualifying_intelligences))
                cursor.execute(query % format_strings, tuple(qualifying_intelligences))
                branch_ids = [row[0] for row in cursor.fetchall()]
                return branch_ids
        except Exception as e:
            print(f"Error obteniendo branches de intelligences: {e}")
            return []

    @staticmethod
    def get_all_branch_for_question_word_key():
        qualifying_intelligences = BranchService.get_all_branch_for_intelligence()

        if not qualifying_intelligences:
            return []

        try:
            with mysql.connection.cursor() as cursor:
                # Obtener IDs de preguntas
                query = """SELECT DISTINCT id_questions FROM questions WHERE id_intelligences IN (%s)"""
                format_strings = ",".join(["%s"] * len(qualifying_intelligences))
                cursor.execute(query % format_strings, tuple(qualifying_intelligences))
                question_ids = [row[0] for row in cursor.fetchall()]
                if not question_ids:
                    return []
                # Obtener IDs de WordKey
                query = """SELECT DISTINCT id_word_key FROM question_word_key WHERE id_question IN (%s)"""
                format_strings = ",".join(["%s"] * len(question_ids))
                cursor.execute(query % format_strings, tuple(question_ids))
                word_key_ids = [row[0] for row in cursor.fetchall()]
                if not word_key_ids:
                    return []
                # Obtener IDs de ramas
                query = """SELECT branch_id FROM vistatoptenpalabrasclaveporrama WHERE word_key_id IN (%s)"""
                format_strings = ",".join(["%s"] * len(word_key_ids))
                cursor.execute(query % format_strings, tuple(word_key_ids))
                branch_ids = [row[0] for row in cursor.fetchall()]
                return branch_ids

        except Exception as e:
            print(f"Error obteniendo branches de preguntas: {e}")
            return []

    @staticmethod
    def get_top_three_branch():
        # Obtener ramas de preferencias
        branches_from_preferences = BranchService.get_branch_ids_from_preference_groups()
        # Obtener ramas de inteligencias
        branches_from_intelligence = BranchService.get_all_branch_for_intelligence()
        # Obtener ramas de preguntas y palabras clave
        branches_from_questions_word_key = BranchService.get_all_branch_for_question_word_key()

        # Intersección de ramas filtradas
        common_branches = set(branches_from_preferences) & set(branches_from_intelligence) & set(
            branches_from_questions_word_key)

        if len(common_branches) >= 3:
            result_branches = list(common_branches)[:3]
        else:
            # Contar las ramas presentes en al menos dos listas
            branch_counts = Counter(branches_from_preferences + branches_from_intelligence + branches_from_questions_word_key)
            two_out_of_three_branches = [branch for branch, count in branch_counts.items() if count >= 2]

            result_branches = list(common_branches) + two_out_of_three_branches

            if len(result_branches) >= 3:
                result_branches = result_branches[:3]
            else:
                # Rellenar con ramas únicas si no hay suficientes
                unique_branches = list(set(branches_from_preferences + branches_from_intelligence + branches_from_questions_word_key))
                result_branches = result_branches + unique_branches
                result_branches = result_branches[:3]

        # Obtener detalles de las ramas (id_branch, name, description)
        try:
            with mysql.connection.cursor() as cursor:
                query = """SELECT id_branch, name, description FROM branch WHERE id_branch IN (%s)"""
                format_strings = ",".join(["%s"] * len(result_branches))
                cursor.execute(query % format_strings, tuple(result_branches))
                branches = [Branch(*row).serialize() for row in cursor.fetchall()]
                return branches

        except Exception as e:
            print(f"Error obteniendo detalles de branches: {e}")
            return []