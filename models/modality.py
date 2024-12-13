class Modality:
    def __init__(self, id_modality, modality):
        self.id_modality = id_modality
        self.modality = modality

    def serialize(self):
        return {
            'id_modality': self.id_modality,
            'modality': self.modality
        }