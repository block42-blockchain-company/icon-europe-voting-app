import Poll, { renderList } from './poll.js'
import IconHandler from './iconhandler.js'


function main()
{
  IconHandler.instance.requestScoreReadMethod("exportPolls", {} )
                      .then(renderList)
}

var test_obj =
{
  getIconHandler : function(){
    return new IconHandler();
  }
}
window.test_obj = test_obj;

window.onload = main();
