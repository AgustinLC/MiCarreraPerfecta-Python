class Career:
    def __init__(self, id_career, name, title_intermediate, description, duration_months, id_type_career, id_modality, id_branch, id_range):
        self.id_career = id_career
        self.name = name
        self.title_intermediate = title_intermediate
        self.description = description
        self.duration_months = duration_months
        self.id_type_career = id_type_career
        self.id_modality = id_modality
        self.id_branch = id_branch
        self.id_range = id_range

    def serialize(self):
        return {
            "id_career": self.id_career,
            "name": self.name,
            "title_intermediate": self.title_intermediate,
            "description": self.description,
            "duration_months": self.duration_months,
            "id_type_career": self.id_type_career,
            "id_modality": self.id_modality,
            "id_branch": self.id_branch,
            "id_range": self.id_range
        }