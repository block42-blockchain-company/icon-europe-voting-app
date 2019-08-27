class Poll:
    def __init__(self, id = -1, name = "default" ) -> None:
        self.id_ = id
        self.name_ = name
        self.description_ = str()
        self.candidates_ = dict()

    def addCandidate(self, name: str) -> None:
        self.candidates_[name] = 0

    def vote(self, name: str) -> None:
        self.candidates_[name] = self.candidates_[name] + 1

    def getCandidates(self) -> dict:
        return self.candidates_

    def getName(self) -> str:
        return self.name_
