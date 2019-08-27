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
        # How to generate ID´s for the polls properly?
        return len(loads(self.polls_)) + 1

    @external
    def getPollByName(self, poll_name: str) -> dict:
        poll = Poll()
        for temp_poll in self.polls_:
            if loads(temp_poll).name_ == poll_name:
                poll = loads(temp_poll)
                break

        return {
                "id": poll.id_,
                "name": poll.name_,
                "description": poll.description_,
                "candidates": poll.candidates_
                }

    @external
    def getPollById(self, poll_id: int) -> dict:
        pass

    @external
    def getPolls(self) -> int:
        return len(self.polls_)

    @external
    def addPollOption(self, poll_option: str) -> None:
        current_poll = loads(self.polls_.get(0))
        current_poll.addCandidate(poll_option)
        self.polls_[0] = dumps(current_poll)

    @external
    def getPollOptions(self) -> dict:
        return loads(self.polls_.get(0)).candidates_;

    @external
    def vote(self, poll_name: str, candidate_name: str) -> None:
        loads(self.getPoll(poll_name)).vote(candidate_name)
