from Utils.score_handler import ScoreHandler
import json, os
import datetime as DT

if __name__ == "__main__":

    score_address = "cxd4ae20043df46a1ad8a4f26e4138a8c8cfc042e9" #<-- Replace with your score address
    #cx02716d61c742fa219a5f0e9fa9d98ae56e5a9075 <--- testnet smartcontract

    #keystore_file = "./iconkeystore"
    #password = "@icon111"
    keystore_file = "/work/voting_score/tests/Utils/keystore_voting_test"
    password = "test1_Account"
    poll_duration = 20000  #every ~2 seconds new block generated

    score_handler = ScoreHandler(score_address, keystore_file, password)
    current_block = int(score_handler.getLatestBlock()['height'])
    print("Current Block is " + str(current_block))

    # Creating polls and votes locally
    # Sample Poll
    polls = [
        {
        "name": "Expected staking period",
        "question": "How long do you plan to stake your ICX?",
        "answers": json.dumps(["Less than one month", "More than one month", "More than six months", "More than a year", "More than two years", "More than three years"]),
        "time_frame" : json.dumps({"start": current_block,
                                          "end": current_block + poll_duration})
        },
        {
        "name": "Origin of Users",
        "question": "Where are you from?",
        "answers": json.dumps(["Asia", "Africa", "North America", "South America", "Europe", "Australia", "Antarctica"]),
        "time_frame" : json.dumps({"start": current_block,
                                  "end": current_block + poll_duration})
        },
        {
        "name": "ICON Europe satisfaction",
        "question": 'How satisfied are you with the ICON Europe initiative? Join us in <a href="https://t.me/IconEurope">telegram!</a>',
        "answers": json.dumps(["Not at all Satisfied", "Partly Satisfied", "Satisfied", "More than Satisfied", "Very Satisfied", "What is ICON Europe?"]),
        "time_frame" : json.dumps({"start": current_block,
                                  "end": current_block + poll_duration})
        },
        {
        "name": "ICON involvement",
        "question": "For how long have you been part of the ICON community?",
        "answers": json.dumps(["Less than one month", "More than one month", "More than six months", "More than a year", "Since ICO"]),
        "time_frame" : json.dumps({"start": current_block,
                                  "end": current_block + poll_duration})
        },
        {
        "name": "ICON Usage",
        "question": "How do you plan to use the ICON ecosystem mainly?",
        "answers": json.dumps(["As an investment", "To build on the platform", "To use the platform as a user"]),
        "time_frame" : json.dumps({"start": current_block,
                                  "end": current_block + poll_duration})
        },
    ]
    

    # Sample Votes
    votes = [{
                "poll_id": 0,
                "poll_answer_id": 0
            },
            {
                "poll_id": 0,
                "poll_answer_id": 1
            }]

    # Interaction with SCORE
    score_handler.writeTransaction("removeAllPolls", {})
    score_handler.writeTransaction("createPoll", polls[0])
    score_handler.writeTransaction("vote", votes[0])
    score_handler.readTransaction("exportPolls", {})