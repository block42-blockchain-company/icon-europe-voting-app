
class Poll
{
  constructor( poll_info )
  {
    this.id = poll_info.id;
    this.name = poll_info.name;
    this.question = poll_info.question;
    this.start_date = poll_info.start_date;
    this.end_date = poll_info.end_date;
    this.description = poll_info.description;
    this.candidates = poll_info.candidates;
  }

  render()
  {
    let table = document.getElementById("polls-table");
    let row = table.insertRow();

    for( var key in this)
    {
      // let cell = ;

      if( key == "name")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "start_date")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "end_date")
        row.insertCell().appendChild(document.createTextNode(this[key]));
    }
  }
}



var polls = [];


function storePolls( polls_data )
{
  // console.log(polls_data);
  for( var it in polls_data)
  {
    var poll = new Poll(polls_data[it])
    poll.render();

    polls.push(poll);
  }
}



function main()
{
  var score_address = "cx08bed0a6999a6c3f866d26c1be67e3e1139ba75a"

  var score_handler = new ScoreHandler(keystore, password, score_address);
  score_handler.requestScoreReadMethod("exportPolls", {} ).then(storePolls)



}


window.onload = main();