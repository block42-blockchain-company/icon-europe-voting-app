import datetime as DT


class Poll:
    def __init__(self, id: int, name: str, question: str) -> None:
        self.__id = id
        self.__name = name
        self.__question = question
        self.__description = str()
        self.__candidates = list()
        self.__start = DT.date.today().strftime("%d/%m/%Y")
        self.__end = (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")
        # self.__initiator

    def addCandidate(self, name: str) -> None:
        new_candidate = dict()
        new_candidate["id"] = len(self.__candidates)
        new_candidate["name"] = name
        new_candidate["votes"] = 0
        self.__candidates.append(new_candidate)

    def vote(self, candidate_id: int, sender_balance: int) -> None:
        candidate = self.getCandidateById(candidate_id)
        candidate["votes"] = candidate["votes"] + sender_balance

    def getId(self) -> int:
        return self.__id

    def getCandidates(self) -> dict:
        return self.__candidates

    def getCandidateById(self, id: int):
        for candidate in self.__candidates:
            if candidate["id"] == int(id):
                return candidate

    def getName(self) -> str:
        return self.__name

    def getData(self) -> dict:
        return {
                "id": self.__id,
                "name": self.__name,
                "question": self.__question,
                "description": self.__description,
                "candidates": self.__candidates,
                "start_date": self.__start,
                "end_date": self.__end,
                }
