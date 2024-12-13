class WordsKey:
    def __init__(self, id_word_key, word):
        self.id_word_key = id_word_key
        self.word = word

    def serialize(self):
        return {
            'id_word_key': self.id_word_key,
            'word': self.word
        }