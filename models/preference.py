class Preference:
    def __init__(self, id_preference, name, id_preference_group):
        self.id_preference = id_preference
        self.name = name
        self.id_preference_group = id_preference_group

    def serialize(self):
        return {
            'id_preference': self.id_preference,
            'name': self.name,
            'id_preference_group': self.id_preference_group
        }