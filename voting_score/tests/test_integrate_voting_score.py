import os

from iconsdk.builder.call_builder import CallBuilder
from iconsdk.icon_service import IconService
from iconsdk.libs.in_memory_zip import gen_deploy_data_content
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.builder.transaction_builder import (
    TransactionBuilder,
    DeployTransactionBuilder,
    CallTransactionBuilder,
    MessageTransactionBuilder
)

from tbears.libs.icon_integrate_test import IconIntegrateTestBase, SCORE_INSTALL_ADDRESS

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

def readTransaction(self, method: str, params: []) -> {}:
    call = CallBuilder().from_(self._test1.get_address())\
                    .to(self._score_address)\
                    .method(method)\
                    .params(params)\
                    .build()
    tx_result = self.process_call(call, self.icon_service)
    return tx_result

def writeTransaction(self, method: str, params: []) -> {}:
    transaction = CallTransactionBuilder()\
                  .from_(self._test1.get_address())\
                  .to(self._score_address)\
                  .step_limit(100000000)\
                  .nid(3)\
                  .nonce(100)\
                  .method(method)\
                  .params(params)\
                  .build()
    signed_transaction = SignedTransaction(transaction, self._test1)
    tx_result = self.process_transaction(signed_transaction, self.icon_service)

    assert 'status' in tx_result
    assert 1 == tx_result['status']

    return tx_result

# Test cases are written in 3 parts:
#   Setup
#   Execute
#   Verify
#
class TestVotingScore(IconIntegrateTestBase):
    TEST_HTTP_ENDPOINT_URI_V3 = "http://127.0.0.1:9000/api/v3"
    SCORE_PROJECT= os.path.abspath(os.path.join(DIR_PATH, '..'))

    def setUp(self):
        super().setUp()

        self.icon_service = None
        # if you want to send request to network, uncomment next line and set self.TEST_HTTP_ENDPOINT_URI_V3
        # self.icon_service = IconService(HTTPProvider(self.TEST_HTTP_ENDPOINT_URI_V3))

        # install SCORE
        self._score_address = self._deploy_score()['scoreAddress']

    def _deploy_score(self, to: str = SCORE_INSTALL_ADDRESS) -> dict:
        # Generates an instance of transaction for deploying SCORE.
        transaction = DeployTransactionBuilder() \
            .from_(self._test1.get_address()) \
            .to(to) \
            .step_limit(100_000_000_000) \
            .nid(3) \
            .nonce(100) \
            .content_type("application/zip") \
            .content(gen_deploy_data_content(self.SCORE_PROJECT)) \
            .build()

        # Returns the signed transaction object having a signature
        signed_transaction = SignedTransaction(transaction, self._test1)

        # process the transaction in local
        tx_result = self.process_transaction(signed_transaction, self.icon_service)

        self.assertTrue('status' in tx_result)
        self.assertEqual(1, tx_result['status'])
        self.assertTrue('scoreAddress' in tx_result)

        return tx_result

    def test_score_update(self):
        # update SCORE
        tx_result = self._deploy_score(self._score_address)

        self.assertEqual(self._score_address, tx_result['scoreAddress'])

    def test_createPoll(self):
        pollName = "BestPizza"
        pollQuestion = "What is the best pizza in the world?"
        pollsBefore = readTransaction(self, "exportPolls", {})

        writeTransaction(self, "createPoll", {"poll_name": pollName, "poll_question": pollQuestion})

        poll = readTransaction(self, "exportPollsByName", {"poll_name": pollName})
        pollsAfter = readTransaction(self, "exportPolls", {})
        self.assertEqual(len(pollsBefore) + 1, len(pollsAfter))
        #print("poll: ", poll)
        #print("poll.question: ", poll["question"])
        self.assertEqual(poll["question"], pollQuestion)

    def test_removePoll(self):
        pollName = "President"
        pollQuestion = "Who should lead ICON-Republic?"
        writeTransaction(self, "createPoll", {"poll_name": pollName, "poll_question": pollQuestion})

        writeTransaction(self, "removePoll", {"poll_id": 0})

        polls = readTransaction(self, "exportPolls", {})
        self.assertEqual(len(polls), 0)

    def test_removeAllPolls(self):
        pollName = "Moon"
        pollQuestion = "When moon?"
        writeTransaction(self, "createPoll", {"poll_name": pollName + "1", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "2", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "3", "poll_question": pollQuestion})

        writeTransaction(self, "removeAllPolls", {})

        polls = readTransaction(self, "exportPolls", {})
        self.assertEqual(len(polls), 0)

    def test_exportPolls(self):
        pollName = "RealNakamoto"
        pollQuestion = "Who is the real Nakamoto?"
        writeTransaction(self, "createPoll", {"poll_name": pollName + "1", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "2", "poll_question": pollQuestion})

        polls = readTransaction(self, "exportPolls", {})

        self.assertEqual(len(polls), 2)
        self.assertEqual(polls[0]["name"], pollName + "1")
        self.assertEqual(polls[1]["name"], pollName + "2")
        self.assertEqual(polls[1]["question"], pollQuestion)
        self.assertEqual(polls[1]["question"], pollQuestion)

    def test_exportPollById(self):
        pollName = "FiatOrCrypto"
        pollQuestion = "What is better for our future - fiat or crypto?"
        writeTransaction(self, "createPoll", {"poll_name": pollName, "poll_question": pollQuestion})

        poll = readTransaction(self, "exportPollById", {"poll_id": 0})

        self.assertEqual(poll["name"], pollName)

    def test_exportPollsByName(self):
        pollName = "EfficientCar"
        pollQuestion = "What is the most efficient car?"
        writeTransaction(self, "createPoll", {"poll_name": pollName + "1", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "2", "poll_question": pollQuestion})

        poll = readTransaction(self, "exportPollsByName", {"poll_name": pollName + "2"})

        self.assertEqual(poll["name"], pollName + "2")
        self.assertEqual(poll["question"], pollQuestion)

    def test_addPollOption(self):
        pollName = "MakeICONGreatAgain"
        pollQuestion = "Choose the best option for the ecosystem!"
        pollEntry = "Wall"
        writeTransaction(self, "createPoll", {"poll_name": pollName + "1", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "2", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "3", "poll_question": pollQuestion})

        writeTransaction(self, "addPollOption", {"poll_id": 0, "poll_entry": pollEntry})

        polls = readTransaction(self, "exportPolls", {})
        self.assertEqual(len(polls[0]["candidates"]), 1)
        self.assertEqual(polls[0]["candidates"][0]["name"], pollEntry)

    def test_getPollOptions(self):
        pollName = "Dinner"
        pollQuestion = "What should we eat for dinner?"
        pollEntry = "A stone"
        writeTransaction(self, "createPoll", {"poll_name": pollName + "1", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "2", "poll_question": pollQuestion})
        writeTransaction(self, "createPoll", {"poll_name": pollName + "3", "poll_question": pollQuestion})
        writeTransaction(self, "addPollOption", {"poll_id": 0, "poll_entry": pollEntry})

        pollOptions = readTransaction(self, "getPollOptions", {"poll_id": 0})

        self.assertEqual(len(pollOptions), 1)
        self.assertEqual(pollOptions[0]["name"], pollEntry)

    def test_getSenderBalance(self):
        #no idea how to test this yet
        pass

    def test_vote(self):
        pollName = "NewPRep"
        pollQuestion = "Who should replace the malicious P-Rep?"
        pollEntry = "Micky Mouse"
        writeTransaction(self, "createPoll", {"poll_name": pollName, "poll_question": pollQuestion})
        writeTransaction(self, "addPollOption", {"poll_id": 0, "poll_entry": pollEntry})

        writeTransaction(self, "vote", {"poll_id": 0, "poll_entry_id": 0})

        poll = readTransaction(self, "exportPollsByName", {"poll_name": pollName + "2"})
        self.assertNotEqual(poll["candidates"][0]["votes"], 0)
