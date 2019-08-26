from iconservice import *
from pickle import dumps, loads
from .poll import Poll

from .poll import Poll

TAG = 'VotingScore'

#local_scole_address = cxc6c0e79fd57c46c4101a2a786479a84fad45505d

class VotingScore(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self.polls_ = ArrayDB("Polls", db, value_type = bytes)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    def createPoll(self, name: str, candidates: bytes) -> None:
        new_poll = Poll(name)
        candidates = loads(candidates)

        for candidate in candidates:
            new_poll.addCandidate(candidate)
        self.polls_.put(dumps(new_poll))

    @external
    def getPoll(self, name: str) -> bytes:
        for poll in self.polls_:
            if poll.name == name:
                return dumps(poll)
    @external
    def vote(self, poll_name: str, candidate_name: str) -> None:
        loads(self.getPoll(poll_name)).vote(candidate_name)
