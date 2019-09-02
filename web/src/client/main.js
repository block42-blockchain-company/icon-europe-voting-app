
class Poll
{
  constructor( poll_info )
  {
    this.id = parseInt(poll_info.id);
    this.name = poll_info.name;
    this.question = poll_info.question;
    this.start_date = poll_info.start_date;
    this.end_date = poll_info.end_date;
    this.description = poll_info.description;
    this.candidates = poll_info.candidates;
  }

  render()
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

    row.addEventListener( "click", this.openDetailView);

  }

  openDetailView()
  {
      let poll = getPollByID( parseInt(this.id.split("-")[1])) //split id from string --> maybe write function to this???!?

      document.getElementsByClassName("poll-title")[0].innerHTML = poll.name;
      document.getElementsByClassName("poll-question")[0].innerHTML = poll.question;
      


      $('#poll-modal').modal("toggle");


  }
}

var polls = [];

function storePolls( polls_data )
{
  for( var it in polls_data)
  {
    var poll = new Poll(polls_data[it])
    poll.render();

    polls.push(poll);
  }
}

function getPollByID( poll_id )
{
  for( let obj in polls)
    if(polls[obj].id === poll_id)
      return polls[obj]
}



function main()
{
  var score_address = "cx08bed0a6999a6c3f866d26c1be67e3e1139ba75a"

  var score_handler = new ScoreHandler(keystore, password, score_address);
  score_handler.requestScoreReadMethod("exportPolls", {} ).then(storePolls)



}


window.onload = main();
