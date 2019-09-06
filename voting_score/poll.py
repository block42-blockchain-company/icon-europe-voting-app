class Poll:
    def __init__(self, obj: dict) -> None:
        self.__id = obj['id']
        self.__name = obj['name']
        self.__question = obj['question']
        self.__description = str()
        self.__answers = self.addAnswers(obj['answers']);
        self.__timestamp = obj['timestamp'];
        self.__initiator = obj['initiator']

    def addAnswers(self, answers: list) -> None:
        temp_list = []

        for obj in answers:
            new_answer = dict()
            new_answer["id"] = len(temp_list)
            new_answer["name"] = obj
            new_answer["votes"] = 0
            temp_list.append(new_answer)

        return temp_list

    def vote(self, answer_id: int, sender_balance: int) -> None:
        answer = self.getAnswerById(answer_id)
        answer["votes"] = answer["votes"] + sender_balance

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
                }

    @staticmethod
    def deserialize(obj: dict) -> 'Poll':
        poll = Poll(obj)
        poll.__answers = obj['answers']
        return poll
