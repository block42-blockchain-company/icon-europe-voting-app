from iconservice import *

from .poll import Poll

TAG = 'VotingScore'


class VotingScore(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.polls_ = ArrayDB("Polls", db, value_type = str)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def createPoll(self, name: str, question: str, answers: str, timestamp: str) -> None:
        poll_dict = {
            "id": self.generatePollID(),
            "name": name,
            "question": question,
            "answers" : json_loads(answers),
            "timestamp": json_loads(timestamp),
            "initiator": str(self.msg.sender)
        }
        self.polls_.put(json_dumps(Poll(poll_dict, self.db).serialize()))

    def generatePollID(self) -> int:
        return len(self.polls_)

    @external
    def removeAllPolls(self) -> None:
        for it in range(len(self.polls_)):
            Poll.removeVotes(it, self.db)
            self.polls_.pop()

    @external( readonly=True)
    def exportPolls(self) -> list:
        polls = list()
        for it in range(len(self.polls_)):
            poll = json_loads(self.polls_[it])
            poll["voters"] = Poll.exportVotes(it, self)
            polls.append(poll)
        return polls

    @external(readonly=True)
    def getPollAnswers(self, poll_id: int) -> dict:
        poll = Poll.deserialize(json_loads(self.polls_.get(poll_id)))
        return poll.getAnswers()

    @external(readonly=True)
    def getSenderBalance(self) -> int:
        return self.icx.get_balance(self.msg.sender)

    @external(readonly=False)
    def vote(self, poll_id: int, poll_answer_id: int) -> None:
        sender_address = self.msg.sender
        sender_balance = self.icx.get_balance(sender_address)
        if(sender_balance > 0):
            poll = Poll(json_loads(self.polls_.get(poll_id)), self.db)
            poll.vote(poll_answer_id, str(sender_address))
        else:
            revert("Throw some fking exception. Like ´no founds, my dear´")
