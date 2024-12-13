class Questions:
    def __init__(self, id_questions, id_intelligence,questions, order_number):
        self.id_questions = id_questions
        self.id_intelligence = id_intelligence
        self.questions = questions
        self.order_number = order_number

    def serialize(self):
        return {
            "id_questions": self.id_questions,
            "id_intelligence": self.id_intelligence,
            "questions": self.questions,
            "order_number": self.order_number
        }