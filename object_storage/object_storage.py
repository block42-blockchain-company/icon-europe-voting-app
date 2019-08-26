from iconservice import *
from pickle import *

TAG = 'ObjectStorage'

class ObjectStorage(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._elections = ArrayDB("elections", db, value_type=bytes)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        for personBytes in self._elections:
            decodedPerson=loads(personBytes)
            Logger.debug(f'Hello, world', personBytes)
            Logger.debug(f'Hello, world', decodedPerson.name)

            return decodedPerson.name
        return "hahah fail"
    
    @external
    def createPerson(self, name: str) -> None:
        newPerson = Person(name)
        newPersonBytes = dumps(newPerson)
        self._elections.put(newPersonBytes)

    @external
    def createElection(self, name: str) -> None:
        newElection = Election(name)
        newElection.addCandidate("DonaldTrump")
        newElection.addCandidate("MickyMaus")
        newElection.addCandidate("Tomaz")
        self._elections.put(dumps(newElection))
    
    @external
    def vote(self, name: str) -> None:
        currentElectionBytes = self._elections.get(0)
        currenteElection = loads(currentElectionBytes)
        currenteElection.vote(name)
        self._elections[0] = dumps(currenteElection) 

    @external(readonly=True)
    def getCurrentStateOfElection(self) -> dict:
        currentElectionBytes = self._elections.get(0)
        currentElection = loads(currentElectionBytes)
        return currentElection.candidates



class Person:
    def __init__(self, name: str):
        self.name = name

    def myfunc(self) -> None:
        print("Hello my name is " + self.name)


class Election:
    def __init__(self, name: str):
        self.name = name
        self.candidates = dict()

    def addCandidate(self, name: str) -> None:
        self.candidates[name] = 0

    def vote(self, name: str) -> None:
        self.candidates[name] = self.candidates[name] + 1

    def getCandidates(self) -> dict:
        return self.candidates
