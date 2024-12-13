class QuestionWordKey:
    def __init__(self, id_question_word_key, id_question, id_word_key):
        self.id_question_word_key = id_question_word_key
        self.id_word_key = id_word_key
        self.id_question = id_question

    def serialize(self):
        return {
            'id_question_word_key': self.id_question_word_key,
            'id_word_key': self.id_word_key,
            'id_question': self.id_question,
        }