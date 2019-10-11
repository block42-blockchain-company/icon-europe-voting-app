import Poll, { renderPolls, storePolls } from './poll.js'
import IconHandler from './iconhandler.js'
import {renderCookiesAgreement} from './cookieUtils.js'


function main()
{
  IconHandler.instance.requestScoreReadMethod("exportPolls", {} )
                      .then(storePolls)
                      .then(renderPolls)
                      .then(renderCookiesAgreement)
}

window.onload = main();
