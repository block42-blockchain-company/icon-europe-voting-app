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
        pass

    def test_generatePollID(self):
        pass

    def test_removePoll(self):
        pass

    def test_removeAllPolls(self):
        pass

    def test_exportPolls(self):
        pass

    def test_exportPollById(self):
        pass

    def test_exportPollsByName(self):
        pass

    def test_addPollOption(self):
        pass

    def test_getPollOptions(self):
        pass

    def test_getSenderBalance(self):
        pass

    def test_vote(self):
        pass