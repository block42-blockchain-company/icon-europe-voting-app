import * as constants from './constants.js';

const iconService = window['icon-sdk-js'];
// const httpProvider = new iconService(new iconService.HttpProvider('https://bicon.net.solidwallet.io/api/v3'))
const httpProvider = new iconService(new iconService.HttpProvider('http://127.0.0.1:9000/api/v3'))
const iconBuilder = iconService.IconBuilder;
const iconConverter = iconService.IconConverter;

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

  static get instance()
  {
    if(!_instance)
    {
      new IconHandler();
    }
    return _instance;
  }

  get wallet()
  {
    return this._wallet;
  }


  async requestScoreReadMethod( method, params )
  {
    let callBuilder = new iconBuilder.CallBuilder;

    let call_obj = callBuilder
                    .to(this._score_address)
                    .method(method)
                    .params(params)
                    .build();


    return await httpProvider.call(call_obj).execute();
  }

  async requestScoreWriteMethod( method, params )
  {
    let callBuilder = new iconBuilder.CallTransactionBuilder;

    let call_obj = callBuilder
                   .from(this._wallet)
                   .to(this._score_address)
                   .stepLimit(iconConverter.toBigNumber('2000000'))
                   .nid(iconConverter.toBigNumber('3'))
                   .nonce(iconConverter.toBigNumber('1'))
                   .version(iconConverter.toBigNumber('3'))
                   .timestamp((new Date()).getTime() * 1000)
                   .method(method)
                   .params(params)
                   .build();

    let json_rpc = JSON.stringify({
                    "jsonrpc": "2.0",
                    "method": method,
                    "params": iconConverter.toRawTransaction(call_obj),
                    "id": 50889
                });

    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_JSON-RPC',
            payload: json_rpc
        }
    }))


  }
}

function bindWalletRequestButton()
{
  //dispatch request
  constants.REQUEST_ADDRESS_BUTTON.addEventListener("click", requestWallet)

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
    constants.REQUEST_ADDRESS_BUTTON.innerHTML = response.payload;
    constants.REQUEST_ADDRESS_BUTTON.removeEventListener("click", requestWallet);
  }
}
