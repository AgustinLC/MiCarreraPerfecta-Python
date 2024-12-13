class PreferenceGroup:
    def __init__(self, id_preference_group, group, question):
        self.id_preference_group = id_preference_group
        self.group = group
        self.question = question

    def serialize(self):
        return {
            'id_preference_group': self.id_preference_group,
            'group': self.group,
            'question': self.question,
        }