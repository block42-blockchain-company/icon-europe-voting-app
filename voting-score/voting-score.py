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
    def createPoll(self, poll_name: str) -> None:
        new_poll = Poll(self.generatePollID(), poll_name)
        self.polls_.put(dumps(new_poll))

    @external
    def generatePollID(self) -> int:
        return len(self.polls_)

    @external
    def removePoll(self, poll_id: int) -> bool:
        self.polls_.pop()

    @external
    def removeAllPolls(self) -> None:
        for poll in self.polls_:
            self.polls_.pop()

    @external
    def exportPolls(self) -> list:
        """
        Export all polls in the SCORE and makes it human readable
        """
        polls = list()

        for poll in self.polls_:
            polls.append(loads(poll).getData())

        return polls

    @external
    def exportPollById(self, poll_id: int) -> dict:
        """
        Export one and only specific Poll from SCORE
        """
        pass

    # --------------------------------------------------------------------------
    # # BUG:  Need to work on this one, since 2 polls could have the same name
    # --------------------------------------------------------------------------
    @external
    def exportPollsByName(self, poll_name: str) -> dict:
        """
        Exports 0,1 or more human-readable Polls
        """
        poll = Poll()

        for temp_poll in self.polls_:
            if loads(temp_poll).name_ == poll_name:
                poll = loads(temp_poll)
                break

        return poll.getData()

    @external
    def addPollOption(self, poll_id: int, poll_entry: str) -> None:
        current_poll = loads(self.polls_.get(poll_id - 1))
        current_poll.addCandidate(poll_entry)
        self.polls_[poll_id - 1] = dumps(current_poll)

    @external
    def getPollOptions(self) -> dict:
        return loads(self.polls_.get(0)).candidates_

    @external
    def getSenderBalance(self) -> int:
        return self.icx.get_balance(self.msg.sender)

    @external
    def vote(self, poll_id: int, poll_entry_id: str) -> None:
        sender_balance = self.icx.get_balance(self.msg.sender)
        if(sender_balance > 0):
            poll = loads(self.polls_.get(poll_id - 1))
            poll.vote(poll_entry_id, sender_balance)
            self.polls_[poll_id - 1] = dumps(poll)
        else:
            revert("Throw some fking exception. Like, no founds, you poor MOFO")
