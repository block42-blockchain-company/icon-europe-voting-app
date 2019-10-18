from iconservice import *

from .poll import Poll

TAG = 'VotingScore'


class VotingScore(IconScoreBase):

    @eventlog
    def VoteEvent(self, voter: Address, poll_id: int, answer_id: int) -> None:
        pass

    @eventlog
    def PollCreateEvent(self, name: str) -> None:
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.polls_ = ArrayDB("Polls", db, value_type = str)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    def checkPollActive(self, poll_id: int) -> bool:
        poll_end_block = Poll(json_loads(self.polls_.get(poll_id)), self.db).getPollEndBlock()
        poll_start_block = Poll(json_loads(self.polls_.get(poll_id)), self.db).getPollStartBlock()

        if(self.block_height <= poll_end_block and self.block_height >= poll_start_block):
            return True
        else:
            return False

    @external(readonly=False)
    def createPoll(self, name: str, question: str, answers: str, time_frame: str) -> None:
        poll_dict = {
            "id": self.generatePollID(),
            "name": name,
            "question": question,
            "answers" : json_loads(answers),
            "time_frame": json_loads(time_frame),
            "initiator": str(self.msg.sender)
        }
        self.polls_.put(json_dumps(Poll(poll_dict, self.db).serialize()))
        self.PollCreateEvent(name)

    def generatePollID(self) -> int:
        return len(self.polls_)

    @external
    def removeAllPolls(self) -> None:
        if self.msg.sender == self.owner:
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

        if(self.checkPollActive(poll_id) == False):
            revert("Throw some fking exception. Like ´Poll is already finished, my dear´")

        if(sender_balance > 0):
            poll = Poll(json_loads(self.polls_.get(poll_id)), self.db)
            poll.vote(poll_answer_id, str(sender_address))
            self.VoteEvent(sender_address, poll_id, poll_answer_id)
        else:
            revert("Throw some fking exception. Like ´no funds, my dear´")
