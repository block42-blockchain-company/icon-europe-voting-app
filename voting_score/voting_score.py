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
        self.polls_.put(json_dumps(Poll(poll_dict).serialize()))

    def generatePollID(self) -> int:
        return len(self.polls_)

    @external
    def removeAllPolls(self) -> None:
        for poll in self.polls_:
            self.polls_.pop()

    @external(readonly=True)
    def exportPolls(self) -> list:
        """
        Export all polls in the SCORE and makes it human readable
        """
        polls = list()

        for poll in self.polls_:
            polls.append(poll)

        return polls

    @external(readonly=True)
    def getPollAnswers(self, poll_id: int) -> dict:
        poll = Poll.deserialize(json_loads(self.polls_.get(poll_id)))
        return poll.getAnswers()

    @external(readonly=True)
    def getSenderBalance(self) -> int:
        return self.icx.get_balance(self.msg.sender)

    @external
    def vote(self, poll_id: int, poll_answer_id: int) -> None:
        sender_balance = self.icx.get_balance(self.msg.sender)
        if(sender_balance > 0):
            poll = Poll.deserialize(json_loads(self.polls_.get(poll_id)))
            poll.vote(poll_answer_id, sender_balance)
            self.polls_[poll_id] = json_dumps(poll.serialize())
        else:
            revert("Throw some fking exception. Like ´no founds, my dear´")
