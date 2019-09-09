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
import pprint



class ScoreHandler:

    # icon_service = IconService(HTTPProvider("https://bicon.net.solidwallet.io", 3))
    icon_service = IconService(HTTPProvider("http://localhost:9000", 3))
    pp = pprint.PrettyPrinter(indent=4)

    def __init__(self, score_address: str, keystore_file: str, password: str) -> None:
        self.score_address_ = score_address
        self.wallet_ = KeyWallet.load(keystore_file, password)

    def readTransaction(self, method: str, params: []) -> {}:
        call = CallBuilder()\
                        .to(self.score_address_)\
                        .method(method)\
                        .params(params)\
                        .build()
        result = self.icon_service.call(call)
        for obj in result:
            self.pp.pprint(obj)
        return result

    def writeTransaction(self, method: str, params: []) -> {}:
        transaction = CallTransactionBuilder()\
                      .from_(self.wallet_.get_address())\
                      .to(self.score_address_)\
                      .step_limit(10000000)\
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
