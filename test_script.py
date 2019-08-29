from score_handler import ScoreHandler

if __name__ == "__main__":

    # "cxc6c0e79fd57c46c410a1a2a786479a84fad45505d" #<-- old old
    # cxf68897091500f05beb5cece709e330f4664386c8 --> old
    # cx8fbe6da6369935db85970b8da8798526276982a4 ---> new one

    # cx3720aa917514d93ba30152cfd5054fbb557a5bd8 <--- unsused one with 4 empty polls

    score_address = "cxcd3e29312307f1c9bbe3790609342797c4cc70ad" #<-- Replace with your score address
    keystore_file = "./keystore_test2"
    password = "@icon123"


    score_handler = ScoreHandler(score_address, keystore_file, password);


    # Sample for creating poll
    create_poll = {"poll_name": "President elections"}

    # Sample for creating polls entries
    # {poll_id : int
    #  poll_entry : string}
    poll_option = {
                "poll_id": "0",
                "poll_entry": "Satoshi Nakomoto"
                }
    poll_option1 = {
                "poll_id": "0",
                "poll_entry": "Bob Marley"
                }
    poll_option2 = {
                "poll_id": "0",
                "poll_entry": "Donald Trump"
                }

    # Vote sample object
    # {poll_id : candidate_id,
    #  poll_entry_id : }
    vote_obj = {
            "poll_id": "0",
            "poll_entry_id": "1"
                }

    get_poll_options = { "poll_id": "0"}

    # score_handler.writeTransaction("createPoll", create_polls
    # score_handler.writeTransaction("createPoll", create_poll)
    # score_handler.writeTransaction("addPollOption", poll_options
    # score_handler.writeTransaction("addPollOption", poll_option1)
    # score_handler.writeTransaction("addPollOption", poll_option2)
    # score_handler.readTransaction("exportPolls", {})
    # score_handler.readTransaction("getSenderBalance", {})
    score_handler.writeTransaction("vote", vote_obj)
    # score_handler.readTransaction("exportPolls", {})
    # score_handler.readTransaction("removePoll", {"poll_id": "0"})
    # score_handler.readTransaction("getPollByName", poll_name)
    score_handler.readTransaction("getPollOptions", get_poll_options)
