class TypeCareer:
    def __init__(self, id_type_career, name):
        self.id_type_career = id_type_career
        self.name = name

    def serialize(self):
        return {
            'id_type_career': self.id_type_career,
            'name': self.name
        }