import * as constants from './constants.js';

const iconService = window['icon-sdk-js'];
// const httpProvider = new iconService(new iconService.HttpProvider('https://bicon.net.solidwallet.io/api/v3'))
const httpProvider = new iconService(new iconService.HttpProvider('http://127.0.0.1:9000/api/v3'))
const iconBuilder = iconService.IconBuilder;

//singletone instance
let _instance = null;

export default class IconHandler
{
  constructor()
  {
    if(!_instance)
    {
      _instance = this;

      this._wallet = null;
      this._score_address = constants.SCORE_ADDRESS;

      bindWalletRequestButton();
    }
    else
      return _instance;
  }

  async requestScoreReadMethod( method, params )
  {
    var callBuilder = new iconBuilder.CallBuilder;

    var call_obj = callBuilder
                    .to(this._score_address)
                    .method(method)
                    .params(params)
                    .build();


    return await httpProvider.call(call_obj).execute();
  }

  async requestScoreWriteMethod( method, params )
  {

  }
}

function bindWalletRequestButton()
{
  //dispatch request
  constants.request_address_button.addEventListener("click", requestWallet)

  //catch response
  window.addEventListener(constants.ICONEX_RESPONSE, responseWallet, false)

}


function requestWallet()
{
  window.dispatchEvent(constants.HAS_ACCOUNT_REQUEST);
}

function responseWallet(ev)
{
  let response = ev.detail;

  if(response.type == constants.HAS_ACCOUNT_RESPONSE)
  {
    if(response.payload.hasAccount)
    window.dispatchEvent(constants.ADDRESS_REQUEST);
  }
  else if ( response.type == constants.ADDRESS_RESPONSE )
  {
    _instance._wallet = response.payload;
    constants.request_address_button.innerHTML = response.payload;
    constants.request_address_button.removeEventListener("click", requestWallet);
  }
}
