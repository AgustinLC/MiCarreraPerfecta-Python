class BranchIntelligence:
    def __init__(self, id_branch_intelligence, id_intelligence, id_branch):
        self.id_branch_intelligence = id_branch_intelligence
        self.id_intelligence = id_intelligence
        self.id_branch = id_branch

    def serialize(self):
        return {
            "id_branch_intelligence": self.id_branch_intelligence,
            "id_intelligence": self.id_intelligence,
            "id_branch": self.id_branch
        }