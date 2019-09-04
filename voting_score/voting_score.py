from iconservice import *
from pickle import dumps, loads
from .poll import Poll

from .poll import Poll

TAG = 'VotingScore'


class VotingScore(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.polls_ = ArrayDB("Polls", db, value_type = bytes)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def createPoll(self, poll_name: str, poll_question: str) -> None:
        new_poll = Poll(self.generatePollID(), poll_name, poll_question)
        self.polls_.put(dumps(new_poll))

    def generatePollID(self) -> int:
        return len(self.polls_)

    @external
    def removePoll(self, poll_id: int) -> bool: #why is poll_id needed?
        self.polls_.pop()

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
            polls.append(loads(poll).getData())

        return polls

    @external(readonly=True)
    def exportPollById(self, poll_id: int) -> dict:
        """
        Export one and only specific Poll from SCORE
        """
        pass

    # --------------------------------------------------------------------------
    # # BUG:  Need to work on this one, since 2 polls could have the same name
    # --------------------------------------------------------------------------
    @external(readonly=True)
    def exportPollsByName(self, poll_name: str) -> dict:
        """
        Exports 0,1 or more human-readable Polls
        """
        poll = {}

        for temp_poll in self.polls_:
            if loads(temp_poll).getName() == poll_name:
                poll = loads(temp_poll)
                break

        return poll.getData()

    @external
    def addPollOption(self, poll_id: int, poll_entry: str) -> None:
        current_poll = loads(self.polls_.get(poll_id))
        current_poll.addCandidate(poll_entry)
        self.polls_[poll_id] = dumps(current_poll)

    @external(readonly=True)
    def getPollOptions(self, poll_id: int) -> dict:
        return loads(self.polls_.get(poll_id)).getCandidates()

    @external(readonly=True)
    def getSenderBalance(self) -> int:
        return self.icx.get_balance(self.msg.sender)

    @external
    def vote(self, poll_id: int, poll_entry_id: str) -> None:
        sender_balance = self.icx.get_balance(self.msg.sender)
        print("sender_balance: ", sender_balance)
        if(sender_balance > 0):
            poll = loads(self.polls_.get(poll_id - 1))
            poll.vote(poll_entry_id, sender_balance)
            self.polls_[poll_id - 1] = dumps(poll)
        else:
            revert("Throw some fking exception. Like ´no founds, my dear´")
