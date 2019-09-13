import Poll, { renderPolls, storePolls } from './poll.js'
import IconHandler from './iconhandler.js'


function main()
{
  IconHandler.instance.requestScoreReadMethod("exportPolls", {} )
                      .then(storePolls)
                      .then(renderPolls)
}

window.onload = main();
