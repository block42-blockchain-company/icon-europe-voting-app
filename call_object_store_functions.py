import time
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
icon_service = IconService(HTTPProvider("http://localhost:9000", 3))
from iconsdk.wallet.wallet import KeyWallet

from iconsdk.builder.transaction_builder import (
    TransactionBuilder,
    DeployTransactionBuilder,
    CallTransactionBuilder,
    MessageTransactionBuilder
)
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.builder.call_builder import CallBuilder

scoreAddress = "cxc6c0e79fd57c46c4101a2a786479a84fad45505d" #<-- Replace with your score address

wallet = KeyWallet.load("./keystore_test1", "test1_Account")


def readTransaction(method: str, params: []) -> {}:
    call = CallBuilder().from_(wallet.get_address())\
                    .to(scoreAddress)\
                    .method(method)\
                    .params(params)\
                    .build()
    result =  icon_service.call(call)
    print(result)
    return result

def writeTransaction(method: str, params: []) -> {}:
    transaction = CallTransactionBuilder()\
                  .from_(wallet.get_address())\
                  .to(scoreAddress)\
                  .step_limit(100000000)\
                  .nid(3)\
                  .nonce(100)\
                  .method(method)\
                  .params(params)\
                  .build()
    signed_transaction = SignedTransaction(transaction, wallet)
    tx_hash = icon_service.send_transaction(signed_transaction)
    time.sleep(10)
    result = icon_service.get_transaction_result(tx_hash)
    print(result)
    return result

#writeTransaction("createPerson", {"name": "Richard"})
#readTransaction("hello", {})

writeTransaction("createElection", {"name": "Nationalratswahl2"})
print("---------------------------")
readTransaction("getCurrentStateOfElection", {})
print("---------------------------")
writeTransaction("vote", {"name": "Tomaz"})
print("---------------------------")
writeTransaction("vote", {"name": "MickyMaus"})
print("---------------------------")
writeTransaction("vote", {"name": "Tomaz"})
print("---------------------------")
print("---------------------------")
readTransaction("getCurrentStateOfElection", {})


print("SUCCESS!")
print("EVERYTHING WORKED, WELL DONE ICONIST.")
