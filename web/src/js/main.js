import Poll, { storePolls } from './poll.js'
import IconHandler from './iconhandler.js'


function main()
{
  let score_handler = new IconHandler();
  score_handler.requestScoreReadMethod("exportPolls", {} ).then(storePolls)
}

var test_obj =
{
  getIconHandler : function(){
    return new IconHandler();
  }
}
window.test_obj = test_obj;

window.onload = main();
