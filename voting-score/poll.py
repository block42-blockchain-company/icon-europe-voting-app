class Poll:
    def __init__(self, name : str ):
        seld.id_ = int()
        self.name_ = name
        self.candidates_ = dict()

    def addCandidate(self, name: str) -> None:
        self.candidates_[name] = 0

    def vote(self, name: str) -> None:
        self.candidates_[name] = self.candidates_[name] + 1

    def getCandidates(self) -> dict:
        return self.candidates_
