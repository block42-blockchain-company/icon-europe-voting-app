from score_handler import ScoreHandler

if __name__ == "__main__":

    # "cxc6c0e79fd57c46c410a1a2a786479a84fad45505d" #<-- old old
    # cxf68897091500f05beb5cece709e330f4664386c8 --> old
    # cx8fbe6da6369935db85970b8da8798526276982a4 ---> new one

    # cx3720aa917514d93ba30152cfd5054fbb557a5bd8 <--- unsused one with 4 empty polls

    score_address = "cxf2de4a1813bad480b843db8152f34e22aa40998c" #<-- Replace with your score address
    keystore_file = "./keystore_test1"
    password = "test1_Account"


    score_handler = ScoreHandler(score_address, keystore_file, password);


    # Sample for creating poll
    create_poll = {"poll_name": "President elections"}

    add_question = {"poll_question" : "What was the last show you watched?"}

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

    # score_handler.writeTransaction("createPoll", create_poll)
    # score_handler.writeTransaction("createPoll", create_poll)
    # score_handler.writeTransaction("addPollOption", poll_options
    # score_handler.writeTransaction("addPollOption", poll_option1)
    # score_handler.writeTransaction("addPollOption", poll_option2)
    score_handler.readTransaction("exportPolls", {})

    # score_handler.readTransaction("getSenderBalance", {})
    # score_handler.writeTransaction("vote", vote_obj)
    # score_handler.writeTransaction("removeAllPolls", {})
    # score_handler.readTransaction("exportPolls", {})
    # score_handler.readTransaction("removePoll", {"poll_id": "0"})
    # score_handler.readTransaction("getPollByName", poll_name)
    # score_handler.readTransaction("getPollsOptions", get_poll_options)


    create_poll = {"poll_name": ""}


    new_polls = list();
    new_polls = [
        {
        "poll_name": "ICON President elections",
        "poll_question": "Who should be our president in ICON-Republic?"
        },
        {
        "poll_name": "Last Show",
        "poll_question": "What was the last show you watched?"
        },
        {
        "poll_name": "Favourite Meal",
        "poll_question": "What is your favourite meal?"
        },
        {
        "poll_name": "Rather have...",
        "poll_question": "Would you rather have?"
        },
        {
        "poll_name": "Best fries",
        "poll_question": "Who hast the best fries?"
        },
        {
        "poll_name": "Hair or makeup",
        "poll_question": "Hair or makeup first?"
        },
        {
        "poll_name": "Cat-Dog-Person",
        "poll_question": "Are you a cat person or a dog person?"
        },
        {
        "poll_name": "Favorite ice-cream",
        "poll_question": "What is your favorite ice-cream flavor?"
        },
        {
        "poll_name": "Deep clean",
        "poll_question": "How long has it been since you've deep cleaned you refrigerator?"
        },
        {
        "poll_name": "Favorite candy",
        "poll_question": "What is you favorite kind of candy?"
        },
        {
        "poll_name": "Favorite Pokemon",
        "poll_question": "What is your favorite Pokemon?"
        }
    ]

    # for poll in new_polls:
    #     score_handler.writeTransaction("createPoll", poll)

    # poll_options =[
    #     {
    #         "poll_id": "0",
    #         "poll_entry": "Stranger Things"
    #     },
    #     {
    #         "poll_id": "0",
    #         "poll_entry": "Rick and Morty"
    #     },
    #     {
    #         "poll_id": "0",
    #         "poll_entry": "Tom and Jerry"
    #     },
    #     {
    #         "poll_id": "1",
    #         "poll_entry": "Breakfast"
    #     },
    #     {
    #         "poll_id": "1",
    #         "poll_entry": "Breakfast"
    #     },
    #     {
    #         "poll_id": "1",
    #         "poll_entry": "Lunch"
    #     },
    #     {
    #         "poll_id": "1",
    #         "poll_entry": "Brunch"
    #     },
    #     {
    #         "poll_id": "1",
    #         "poll_entry": "Dinner"
    #     },
    #     {
    #         "poll_id": "2",
    #         "poll_entry": "Personal chef"
    #     },
    #     {
    #         "poll_id": "2",
    #         "poll_entry": "Maid"
    #     },
    #     {
    #         "poll_id": "2",
    #         "poll_entry": "Nanny"
    #     },
    #     {
    #         "poll_id": "2",
    #         "poll_entry": "Lambo"
    #     },
    #     {
    #         "poll_id": "3",
    #         "poll_entry": "Burger King"
    #     },
    #     {
    #         "poll_id": "3",
    #         "poll_entry": "McDonalds"
    #     },
    #     {
    #         "poll_id": "3",
    #         "poll_entry": "KFC"
    #     },
    #     {
    #         "poll_id": "4",
    #         "poll_entry": "Hair"
    #     },
    #     {
    #         "poll_id": "4",
    #         "poll_entry": "Makeup"
    #     },
    #     {
    #         "poll_id": "5",
    #         "poll_entry": "Cat-person"
    #     },
    #     {
    #         "poll_id": "5",
    #         "poll_entry": "Dog-person"
    #     },
    #     {
    #         "poll_id": "5",
    #         "poll_entry": "Dog-person"
    #     },
    #     {
    #         "poll_id": "6",
    #         "poll_entry": "Choclate"
    #     },
    #     {
    #         "poll_id": "6",
    #         "poll_entry": "Vanilla"
    #     },
    #     {
    #         "poll_id": "6",
    #         "poll_entry": "Peach"
    #     },
    #     {
    #         "poll_id": "6",
    #         "poll_entry": "stračitela"
    #     },
    #     {
    #         "poll_id": "7",
    #         "poll_entry": "1 week"
    #     },
    #     {
    #         "poll_id": "7",
    #         "poll_entry": "1 month"
    #     },
    #     {
    #         "poll_id": "7",
    #         "poll_entry": "1 year"
    #     },
    #     {
    #         "poll_id": "7",
    #         "poll_entry": "never"
    #     },
    #     {
    #         "poll_id": "8",
    #         "poll_entry": "LoliPop"
    #     },
    #     {
    #         "poll_id": "8",
    #         "poll_entry": "BonBon"
    #     },
    #     {
    #         "poll_id": "8",
    #         "poll_entry": "Dick"
    #     },
    #     {
    #         "poll_id": "9",
    #         "poll_entry": "Bulbasaur"
    #     },
    #     {
    #         "poll_id": "9",
    #         "poll_entry": "Charmander"
    #     },
    #     {
    #         "poll_id": "9",
    #         "poll_entry": "Wartortle"
    #     }
    #
