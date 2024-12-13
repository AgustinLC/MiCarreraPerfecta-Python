class CampusCareer:
    def __init__(self, id_campus_career, id_campus, id_career, id_requirement):
        self.id_campus_career = id_campus_career
        self.id_campus = id_campus
        self.id_career = id_career
        self.id_requirement = id_requirement

    def serialize(self):
        return {
            'id_campus_career': self.id_campus_career,
            'id_campus': self.id_campus,
            'id_career': self.id_career,
            'id_requirement': self.id_requirement
        }