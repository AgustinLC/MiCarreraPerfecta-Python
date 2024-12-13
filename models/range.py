class Range:
    def __init__(self, id_range, name):
        self.id_range = id_range
        self.name = name

    def serialize(self):
        return {
            'id_range': self.id_range,
            'name': self.name
        }