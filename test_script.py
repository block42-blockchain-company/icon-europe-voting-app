from score_handler import ScoreHandler

if __name__ == "__main__":

    # "cxc6c0e79fd57c46c410a1a2a786479a84fad45505d" #<-- old old
    # cxf68897091500f05beb5cece709e330f4664386c8 --> old
    # cx8fbe6da6369935db85970b8da8798526276982a4 ---> new one

    score_address = "cx8fbe6da6369935db85970b8da8798526276982a4" #<-- Replace with your score address
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

    poll_name = {"poll_name": "President elections day 2"}

    score_handler.writeTransaction("createPoll", poll_name)
    # score_handler.writeTransaction("addPollOption", poll_option)
    # score_handler.writeTransaction("addPollOption", poll_option1)
    # score_handler.writeTransaction("addPollOption", poll_option2)
    score_handler.readTransaction("getPolls", {})
    score_handler.readTransaction("removePoll", {"poll_id": "0"})
    # score_handler.readTransaction("getPollByName", poll_name)
    # score_handler.readTransaction("getPollOptions", {})
