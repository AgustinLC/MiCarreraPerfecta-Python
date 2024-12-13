class CareerWordKey:
    def __init__(self, id_career_word_key, id_career, id_word_key):
        self.id_career_word_key = id_career_word_key
        self.id_career = id_career
        self.id_word_key = id_word_key

    def serialize(self):
        return {
            'id_career_word_key': self.id_career_word_key,
            'id_career': self.id_career,
            'id_word_key': self.id_word_key
        }
