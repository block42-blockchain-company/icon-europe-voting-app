import Poll, { renderList } from './poll.js'
import IconHandler from './iconhandler.js'


function main()
{
  IconHandler.instance.requestScoreReadMethod("exportPolls", {} )
                      .then(renderList)
}

window.onload = main();
