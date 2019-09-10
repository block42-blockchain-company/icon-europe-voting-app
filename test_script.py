from score_handler import ScoreHandler
import json
import datetime as DT

if __name__ == "__main__":

    #cx02716d61c742fa219a5f0e9fa9d98ae56e5a9075 <--- testnet smartcontract

    score_address = "cx41bbbfb3aba3c383e0e2f222203a4c3f462f83e3" #<-- Replace with your score address
    keystore_file = "./keystore_test1"
    password = "test1_Account"
    # keystore_file = "./keystore_test2"
    # password = "@icon123"



    score_handler = ScoreHandler(score_address, keystore_file, password);


    # Sample for creating poll
    create_poll = {
                "name": "ICON President elections",
                "question": "Who should be our president in ICON-Republi",
                "answers": json.dumps(["ena", "dva", "tri"]),
                "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                          "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
                }

    # Vote sample object
    vote_obj = {
                "poll_id": 0,
                "poll_answer_id": 0
                }

    # score_handler.writeTransaction("removeAllPolls", {})


    new_polls = [
        {
        "name": "ICON President elections",
        "question": "Who should be our president in ICON-Republic?",
        "answers": json.dumps(["Donald Trump", "Bob Marley", "Satoshi Nakamoto"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Last Show",
        "question": "What was the last show you watched?",
        "answers": json.dumps(["Stranger Things", "Rick and Morty", "Tom and Jerry"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Favourite Meal",
        "question": "What is your favourite meal?",
        "answers": json.dumps(["Breakfast", "Lunch", "Brunch","Dinner"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Rather have...",
        "question": "Would you rather have?",
        "answers": json.dumps(["Personal chef", "Maid", "Nanny", "Lambo"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Best fries",
        "question": "Who hast the best fries?",
        "answers": json.dumps(["Burger King", "McDonalds", "KFC"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Hair or makeup",
        "question": "Hair or makeup first?",
        "answers": json.dumps(["Hair", "Makeup"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Cat-Dog-Person",
        "question": "Are you a cat person or a dog person?",
        "answers": json.dumps(["Cat-person", "Dog-person"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Favorite ice-cream",
        "question": "What is your favorite ice-cream flavor?",
        "answers": json.dumps(["Choclate", "Vanilla", "Peach","stračitela"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Deep clean",
        "question": "How long has it been since you've deep cleaned you refrigerator?",
        "answers": json.dumps(["1 week", "1 month", "1 year", "never"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Favorite candy",
        "question": "What is you favorite kind of candy?",
        "answers": json.dumps(["LoliPop", "BonBon", "Dick"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
        {
        "name": "Favorite Pokemon",
        "question": "What is your favorite Pokemon?",
        "answers": json.dumps(["Bulbasaur", "Charmander", "Wartortle"]),
        "timestamp" : json.dumps({"start": DT.date.today().strftime("%d/%m/%Y"),
                                  "end": (DT.date.today() + DT.timedelta(days = 31)).strftime("%d/%m/%Y")})
        },
    ]
    # for it in range(len(new_polls)):
    # for it in range(4):
    #     score_handler.writeTransaction("createPoll", new_polls[it])

    score_handler.writeTransaction("vote", vote_obj)
    score_handler.readTransaction("exportPolls", {})
