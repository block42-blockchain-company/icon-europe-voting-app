from iconservice import *

class Poll:
    def __init__(self, obj: dict) -> None:
        self.__id = obj['id']
        self.__name = obj['name']
        self.__question = obj['question']
        self.__description = str()
        self.__answers = self.addAnswers(obj['answers'])
        self.__timestamp = obj['timestamp']
        self.__initiator = obj['initiator']
        self.__votes = dict() if 'votes' not in obj else obj['votes']

    def addAnswers(self, answers: list) -> list:
        temp_list = []
        for answer in answers:
            new_answer = dict()
            if isinstance(answers[0], str):
                new_answer["id"] = len(temp_list)
                new_answer["name"] = answer
                new_answer["votes"] = 0
            else:
                new_answer["id"] = answer["id"]
                new_answer["name"] = answer["name"]
                new_answer["votes"] = answer["votes"]
            temp_list.append(new_answer)
        return temp_list

    def vote(self, answer_id: int, sender_balance: int, sender_address: str) -> None:
        # if voter already voted previously
        if sender_address in self.__votes:
            # substract previous vote
            prev_answer_tuple = next(iter(self.__votes[sender_address].items()))
            prev_answer = self.getAnswerById(prev_answer_tuple[0])
            prev_answer['votes'] = prev_answer['votes'] - prev_answer_tuple[1]
        # add a new vote
        answer = self.getAnswerById(answer_id)
        answer["votes"] = answer["votes"] + sender_balance
        self.__votes[sender_address] = {answer_id: sender_balance}


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
                "description": self.__description,
                "answers": self.__answers,
                "timestamp": self.__timestamp,
                "initiator": self.__initiator,
                "votes": self.__votes,
                }

    @staticmethod
    def deserialize(obj: dict) -> 'Poll':
        return Poll(obj)
