class Branch:
    def __init__(self, id_branch, name, description):
        self.id_branch = id_branch
        self.name = name
        self.description = description

    def serialize(self):
        return {
            'id_branch': self.id_branch,
            'name': self.name,
            'description': self.description
        }