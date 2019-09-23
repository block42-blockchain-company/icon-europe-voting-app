from iconservice import *


class Poll(object):

    _VOTERS = "VOTERS_"
    _VOTERS_CHOICE = "VOTERS_CHOICE_"

    def __init__(self, obj: dict, db: IconScoreDatabase) -> None:
        self.__id = obj['id']
        self.__name = obj['name']
        self.__question = obj['question']
        self.__answers = self.addAnswers(obj['answers'])
        self.__timestamp = obj['timestamp']
        self.__initiator = obj['initiator']
        self.__voters = ArrayDB(f"{self._VOTERS}{self.__id}", db, value_type = str)
        self.__voters_choice = ArrayDB(f"{self._VOTERS_CHOICE}{self.__id}", db, value_type = int)

    def addAnswers(self, answers: list) -> list:
        temp_list = []
        for ans in answers:
            new_answer = dict()
            new_answer["id"] = len(temp_list) if 'id' not in ans else ans['id']
            new_answer["name"] = ans if 'name' not in ans else ans['name']
            temp_list.append(new_answer)
        return temp_list

    def vote(self, answer_id: int, sender_address: str) -> None:
        self.__voters.put(sender_address)
        self.__voters_choice.put(answer_id)

    def getId(self) -> int:
        return self.__id

    def getAnswers(self) -> dict:
        return self.__answers

    def getAnswerById(self, id: int):
        for answer in self.__answers:
            if answer["id"] == int(id):
                return answer

    def getName(self) -> str:
        return self.__name

    def serialize(self) -> dict:
        return {
                "id": self.__id,
                "name": self.__name,
                "question": self.__question,
                "answers": self.__answers,
                "timestamp": self.__timestamp,
                "initiator": self.__initiator,
                }

    @staticmethod
    def removeVotes(poll_id: int, db: IconScoreDatabase) -> None:
        voters = ArrayDB(f"{Poll._VOTERS}{poll_id}", db, value_type = str)
        voters_choice = ArrayDB(f"{Poll._VOTERS_CHOICE}{poll_id}", db, value_type = int)
        while voters:
            voters.pop()
            voters_choice.pop()

    @staticmethod
    def exportVotes(poll_id: int, iconService: IconScoreBase) -> dict:
        voters = ArrayDB(f"{Poll._VOTERS}{poll_id}", iconService.db, value_type = str)
        voters_choice = ArrayDB(f"{Poll._VOTERS_CHOICE}{poll_id}", iconService.db, value_type = int)
        votes = dict()
        for it in range(len(voters)):
            votes[voters[it]] = {voters_choice[it]: iconService.icx.get_balance(Address.from_string(voters[it]))}
        return votes
