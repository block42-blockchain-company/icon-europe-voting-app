from iconservice import *

class Poll:
    def __init__(self, obj: dict) -> None:
        self.__id = obj['id']
        self.__name = obj['name']
        self.__question = obj['question']
        self.__answers = self.addAnswers(obj['answers'])
        self.__timestamp = obj['timestamp']
        self.__initiator = obj['initiator']
        self.__voters = dict() if 'voters' not in obj else obj['voters']

    def addAnswers(self, answers: list) -> list:
        temp_list = []
        for ans in answers:
            new_answer = dict()
            new_answer["id"] = len(temp_list) if 'id' not in ans else ans['id']
            new_answer["name"] = ans if 'name' not in ans else ans['name']
            temp_list.append(new_answer)
        return temp_list

    def vote(self, answer_id: int, sender_balance: int, sender_address: str) -> None:
        self.__voters[sender_address] = answer_id;

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
                "voters": self.__voters,
                }

    @staticmethod
    def deserialize(obj: dict) -> 'Poll':
        return Poll(obj)
