import IconHandler from './iconhandler.js'
import * as constants from './constants.js';

let polls = []; //stores all polls created

export default class Poll
{
  constructor( poll_data )
  {
    this.id = poll_data.id;
    this.name = poll_data.name;
    this.question = poll_data.question;
    this.start_date = poll_data.timestamp.start;
    this.end_date = poll_data.timestamp.end;
    this.description = poll_data.description;
    this.answers = poll_data.answers;
    this.initiator = poll_data.initiator;
    this.votes = poll_data.votes;
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
        if(!IconHandler.instance.wallet)
          row.insertCell().appendChild(document.createTextNode("?"));
        else
        {
          // add '✕' or '✔' to a row
          let span = document.createElement("span");
          span.innerHTML = this.hasUserVoted() ? '&#10004' : '&#10005';
          row.insertCell().appendChild(span);
        }
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
      if(poll.hasUserVoted() &&
         parseInt(Object.keys(poll.votes[IconHandler.instance.wallet])[0] ) === poll.answers[it].id)
      {
        button.classList.remove("btn-light");
        button.classList.add("btn-info");
      }

      //append buttons
      options_list.appendChild(button);
    }

    console.log(vote_button);

    vote_button.DOM.addEventListener("click", poll.vote);
    vote_button.disable();
    vote_button.innerHTML = "Vote";

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
    console.log(this.firstChild);
    let poll_id = document.getElementById("options-list").value;
    let answer_id = this.children[0].value;

    if( getPollByID(poll_id).hasUserVoted() )
    {
      let user_voted_answer = document.getElementsByClassName("btn-info")[0];

      if( user_voted_answer.children[0].value == answer_id )
      {
        vote_button.disable();
        vote_button.innerHTML = "Already voted"
      }
      else
      {
        console.log(vote_button);
        vote_button.innerHTML = "Change Vote";
        vote_button.enable();
      }
    }
    else
    {
      vote_button.enable();
      vote_button.innerHTML = "Vote";
    }
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

  hasUserVoted()
  {
    return this.votes.hasOwnProperty(IconHandler.instance.wallet);
  }
}



export function updateAlreadyVotedCol()
{
  let t_body = constants.TABLE.getElementsByTagName("tbody")[0]

  for( let it in polls )
  {
    // add '✕' or '✔' to a row
    let span = document.createElement("span");
    let poll_DOM = document.getElementById("poll-" + polls[it].id);

    poll_DOM.children[4].innerHTML = ""
    span.innerHTML = polls[it].hasUserVoted() ? '&#10004' : '&#10005';
    poll_DOM.children[4].appendChild(span);
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
    polls.push(new Poll(JSON.parse(polls_data[it])));
}

function getPollByID( poll_id )
{
  for( let obj in polls)
    if(polls[obj].id === poll_id)
      return polls[obj]
}
/**
  Object holding usefull methods for vote Button in Modal
*/
let vote_button = {
  get DOM() {
    return document.getElementById("btn-vote");
  },
  set innerHTML( text ) {
    this.DOM.innerHTML = text;
  },
  disable : function(){
    console.log("disabliing");
    this.DOM.classList.add("disabled");
    this.DOM.setAttribute("disabled", true);
  },
  enable : function() {
    console.log("enabling");
    this.DOM.classList.remove("disabled");
    this.DOM.removeAttribute("disabled");
  }
}
