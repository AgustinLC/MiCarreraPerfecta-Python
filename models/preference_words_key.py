class PreferenceWordsKey:
    def __init__(self, id_p_w_k, id_preference, id_word_key):
        self.id_p_w_k = id_p_w_k
        self.id_preference = id_preference
        self.id_word_key = id_word_key

    def serialize(self):
        return {
            'id_p_w_k': self.id_p_w_k,
            'id_preference': self.id_preference,
            'id_word_key': self.id_word_key
        }