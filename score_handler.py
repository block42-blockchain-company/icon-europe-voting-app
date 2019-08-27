import time
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet

from iconsdk.builder.transaction_builder import (
    TransactionBuilder,
    DeployTransactionBuilder,
    CallTransactionBuilder,
    MessageTransactionBuilder
)
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.builder.call_builder import CallBuilder

from pickle import dumps, loads
import json


class ScoreHandler:

    icon_service = IconService(HTTPProvider("http://localhost:9000", 3))

    def __init__(self, score_address: str, keystore_file: str, password: str) -> None:
        self.score_address_ = score_address
        self.wallet_ = KeyWallet.load(keystore_file, password)

    def readTransaction(self, method: str, params: []) -> {}:
        call = CallBuilder()\
                        .from_(self.wallet_.get_address())\
                        .to(self.score_address_)\
                        .method(method)\
                        .params(params)\
                        .build()
        result = self.icon_service.call(call)
        print(result)
        return result

    def writeTransaction(self, method: str, params: []) -> {}:
        transaction = CallTransactionBuilder()\
                      .from_(self.wallet_.get_address())\
                      .to(self.score_address_)\
                      .step_limit(100000000)\
                      .nid(3)\
                      .nonce(100)\
                      .method(method)\
                      .params(params)\
                      .build()
        signed_transaction = SignedTransaction(transaction, self.wallet_)
        tx_hash = self.icon_service.send_transaction(signed_transaction)
        time.sleep(10)
        result = self.icon_service.get_transaction_result(tx_hash)
        print(result)
        return result



score_address = "cxf68897091500f05beb5cece709e330f4664386c8" #<-- Replace with your score address
keystore_file = "./keystore_test1"
password = "@icon123"

score_handler = ScoreHandler(score_address, keystore_file, password);


#candidates = [ "Satoshi Nakamoto", "Bob Marley", "Donald Trump"]

poll_details = {
              "name" : "poll name",
              "candidate1": "Satoshi Nakamoto",
              "candidate2": "Bob Marley",
              "candidate3": "Donald Trump"}

json_obj = {
  "poll_name": "President elections",
  "candidates": ["Satoshi Nakamoto", "Bob Marley", "Donald Trump"]
}

poll_option = { "poll_option" : "Satoshi Nakamoto"}
poll_option1 = { "poll_option" : "Bob Marley"}
poll_option2 = { "poll_option" : "Donald Trump"}

poll_name = {"poll_name": "President elections"}

score_handler.writeTransaction("createPoll", poll_name)
# score_handler.writeTransaction("addPollOption", poll_option)
# score_handler.writeTransaction("addPollOption", poll_option1)
# score_handler.writeTransaction("addPollOption", poll_option2)
score_handler.readTransaction("getPolls", {})
score_handler.readTransaction("getPollByName", poll_name)
score_handler.readTransaction("getPollOptions", {})
