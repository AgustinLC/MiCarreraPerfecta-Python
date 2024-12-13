class BranchWordKey:
    def __init__(self, id_branch_word_key, id_branch, id_word_key):
        self.id_branch_word_key = id_branch_word_key
        self.id_word_key = id_word_key
        self.id_branch = id_branch

    def serialize(self):
        return {
            'id_branch_word_key': self.id_branch_word_key,
        }