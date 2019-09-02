let polls = [];

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
