import IconHandler from './iconhandler.js'
import * as constants from './constants.js';

let polls = []; //stores all polls created

export default class Poll
{
  constructor( poll_info )
  {
    this.id = parseInt(poll_info.id);
    this.name = poll_info.name;
    this.question = poll_info.question;
    this.start_date = poll_info.start_date;
    this.end_date = poll_info.end_date;
    this.description = poll_info.description;
    this.answers = poll_info.candidates;
  }

  renderListView()
  {
    let tbody = document.getElementById("polls-table").getElementsByTagName("tbody")[0];
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
    }

    row.addEventListener( "click", this.renderDetailView);

  }

  renderDetailView()
  {
      let poll_id = parseInt(this.id.split("-")[1]);
      let poll = getPollByID( poll_id ) //split id from string --> maybe write function to this???!?
      let options_list = document.getElementById("options-list");

      // insert name, valiue and question
      options_list.value = poll_id;
      document.getElementsByClassName("poll-title")[0].innerHTML = poll.name;
      document.getElementsByClassName("poll-question")[0].innerHTML = poll.question;

      //list voting answers
      for( var it in poll.answers)
      {
        if(it == 0 && options_list.children.length) //clear previous buttons
          options_list.innerHTML = "";

        // create buttons
        let label = document.createElement("label");
        label.setAttribute("class", "btn btn-light btn-lg btn-block")
        label.innerHTML = poll.answers[it].name;

        let input = document.createElement("input");
        input.setAttribute("type", "radio");
        input.setAttribute("name", "options");
        input.setAttribute("value", poll.answers[it].id);
        input.setAttribute("autocomplete", "off");
        label.appendChild(input);

        //append buttons
        options_list.appendChild(label);
      }

      constants.VOTE_BUTTON.value = poll_id;
      constants.VOTE_BUTTON.addEventListener("click", poll.vote);

      $('#poll-modal').modal("show"); // toggle on modal
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
        let params =   {
            "poll_id" : poll_id,
            "poll_entry_id" : answer_id
          }

        IconHandler.instance.requestScoreWriteMethod(method, params)
      }
      else
      {
        alert(constants.WALLET_UNCONNECTED)
        $('#poll-modal').modal("hide");
      }
    } catch (e) {
      console.log(e);
      if(e.message == constants.GET_BY_CLASSNAME_UNDEFINED)
      {
        alert("You need to chose one answer");
      }
    }
  }

}

export function renderList( polls_data )
{
  for( var it in polls_data)
  {
    var poll = new Poll(polls_data[it])
    poll.renderListView();

    polls.push(poll);
  }
}

function getPollByID( poll_id )
{
  for( let obj in polls)
    if(polls[obj].id === poll_id)
      return polls[obj]
}
