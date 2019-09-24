import IconHandler from './iconhandler.js'
import * as constants from './constants.js';

let polls = []; //stores all polls created

export default class Poll
{
  constructor( poll_data )
  {
    this.id = parseInt(poll_data.id);
    this.name = poll_data.name;
    this.question = poll_data.question;
    this.start_date = poll_data.timestamp.start;
    this.end_date = poll_data.timestamp.end;
    this.description = poll_data.description;
    this.answers = this.addAnswers( poll_data.answers );
    this.initiator = poll_data.initiator;
    this.votes = poll_data.voters;
  }

  renderListView()
  {
    let tbody = constants.TABLE.getElementsByTagName("tbody")[0];
    let row = tbody.insertRow();

    row.setAttribute("id", "poll-" + this.id);

    for( var key in this)
    {
      if( key == "name")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "start_date")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "end_date")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "initiator")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "votes")
      {
        let span = document.createElement("span");
        span.setAttribute("class", "badge badge-info badge-voted")

        span.innerHTML = (!IconHandler.instance.wallet)
        ? "?"
        : this.hasUserVoted() ? this.answers[this.getUserVote()].name : '&#10005'; // add '✕' or an answer to a row

        row.insertCell().appendChild(span);
      }
    }
    row.addEventListener( "click", this.renderDetailView);
  }

  renderDetailView()
  {
    let poll_id = parseInt(this.id.split("-")[1]);
    let poll = getPollByID( poll_id )
    let options_list = document.getElementById("options-list");


    // insert name, value and question
    options_list.value = poll_id;
    document.getElementsByClassName("poll-title")[0].innerHTML = poll.name;
    document.getElementsByClassName("poll-question")[0].innerHTML = poll.question;

    //list voting answers
    for( var it in poll.answers)
    {
      // clear previous buttons if any
      if(it == 0 && options_list.children.length)
        options_list.innerHTML = "";

      // create button
      let button = poll.createAnswerButton( poll.answers[it] )
      button.addEventListener("click", poll.choseAnswer);

      //highlight button if user voted for that answer already
      if(poll.hasUserVoted() && poll.getUserVote() === poll.answers[it].id)
      {
        button.classList.remove("btn-light");
        button.classList.add("btn-info");
      }

      //append buttons
      options_list.appendChild(button);
    }

    vote_button.DOM.addEventListener("click", poll.vote);
    vote_button.disableVote();

    $('#poll-modal').modal("show");
  }

  createAnswerButton( answer )
  {
    let label = document.createElement("label");
    label.setAttribute("class", "btn btn-light btn-lg btn-block")
    label.innerHTML = answer.name;

    let input = document.createElement("input");
    input.setAttribute("type", "radio");
    input.setAttribute("name", "options");
    input.setAttribute("value", answer.id);
    input.setAttribute("autocomplete", "off");
    label.appendChild(input);

    return label;
  }

  choseAnswer()
  {
    let poll_id = document.getElementById("options-list").value;
    let answer_id = this.children[0].value;

    if( getPollByID(poll_id).hasUserVoted() )
    {
      if( getPollByID(poll_id).getUserVote() == answer_id )
        vote_button.disableVote();
      else
        vote_button.changeVote();
    }
    else
      vote_button.enableVote();
  }

  vote()
  {
    try {
      let poll_id = document.getElementById("options-list").value;
      let answer_id = parseInt(document.getElementsByClassName("active")[0]
                                       .getElementsByTagName("input")[0].value);

      if(IconHandler.instance.wallet)
      {
        let method ="vote";
        let params = {
            "poll_id" : poll_id.toString(),
            "poll_answer_id" : answer_id.toString()
          }

      IconHandler.instance.requestScoreWriteMethod(method, params);

      }
      else
      {
        alert(constants.WALLET_UNCONNECTED)
        $('#poll-modal').modal("hide");
      }
    } catch (e) {
      if(e.message == constants.GET_BY_CLASSNAME_UNDEFINED)
        alert("You need to chose one answer");
    }
  }

  addAnswers( answers_data )
  {
    answers_data.forEach(function(answer){
      Object.keys(answer).forEach(function(key, index){
        if(key === "id")
          answer[key] = parseInt(answer[key])
      });
    })
    return answers_data;
  }

  hasUserVoted()
  {
    return this.votes.hasOwnProperty(IconHandler.instance.wallet);
  }

  getUserVote()
  {
    return parseInt(Object.keys(this.votes[IconHandler.instance.wallet])[0]);
  }
}

export function updateAlreadyVotedCol()
{
  let t_body = constants.TABLE.getElementsByTagName("tbody")[0]

  for( let it in polls )
  {
    // add '✕' or '✔' to a row
    let badge = document.getElementById("poll-" + polls[it].id).children[4].firstChild;
    badge.innerHTML = ( polls[it].hasUserVoted())
    ? polls[it].answers[polls[it].getUserVote()].name
    : '&#10005';
  }
}

export function renderPolls()
{
  for( var it in polls)
    polls[it].renderListView()
}

export function storePolls( polls_data )
{
  polls = [];
  for( var it in polls_data)
    polls.push(new Poll(polls_data[it]));
}

function getPollByID( poll_id )
{
  for( let obj in polls)
    if(polls[obj].id === poll_id)
      return polls[obj]
}

/**
  Object holding usefull methods for vote Button in Modal view
*/
let vote_button = {
  get DOM() {
    return document.getElementById("btn-vote");
  },
  set innerHTML( text ) {
    this.DOM.innerHTML = text;
  },
  disableVote : function(){
    this.DOM.classList.add("disabled");
    this.DOM.setAttribute("disabled", true);
    this.innerHTML = "Vote";
  },
  enableVote : function() {
    this.DOM.classList.remove("disabled");
    this.DOM.removeAttribute("disabled");
    this.innerHTML = "Vote";
  },
  changeVote : function() {
    this.DOM.classList.remove("disabled");
    this.DOM.removeAttribute("disabled");
    this.innerHTML = "Change Vote";
  }
}
