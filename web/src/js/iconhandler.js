import * as constants from './constants.js';
import { updateAlreadyVotedCol, storePolls } from './poll.js'
import * as cookieUtils from './cookieUtils.js';

const iconService = window['icon-sdk-js'];
const httpProvider = new iconService(new iconService.HttpProvider(constants.TESTNET_URL))
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

      this._score_address = constants.SCORE_ADDRESS;

      let wallet_address = cookieUtils.getCookie(constants.COOKIE_NAME_WALLET_ADDRESS);
      if (wallet_address != "")
      {
        this._wallet = wallet_address;
        constants.REQUEST_ADDRESS_BUTTON.innerHTML = wallet_address;
      }
      else
      {
        this._wallet = null;
      }

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

  requestScoreWriteMethod( method, params )
  {
    let callBuilder = new iconBuilder.CallTransactionBuilder;

    let call_obj = callBuilder
                   .from(this._wallet)
                   .to(this._score_address)
                   .nid(iconConverter.toBigNumber('3'))
                   .timestamp((new Date()).getTime() * 1000)
                   .stepLimit(iconConverter.toBigNumber('1000000'))
                   .version(iconConverter.toBigNumber('3'))
                   .method(method)
                   .params(params)
                   .build();


    window.dispatchEvent(new CustomEvent('ICONEX_RELAY_REQUEST', {
        detail: {
            type: 'REQUEST_JSON-RPC',
            payload: {
              jsonrpc: "2.0",
              method: "icx_sendTransaction",
              params: iconConverter.toRawTransaction(call_obj),
              id: 50889
            }
        }
    }));

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
    else
      alert("You need to create a Wallet first")
  }
  else if(response.type == constants.ADDRESS_RESPONSE )
  {
    //save wallet address
    _instance._wallet = response.payload;
    constants.REQUEST_ADDRESS_BUTTON.innerHTML = response.payload;
    cookieUtils.setCookie(constants.COOKIE_NAME_WALLET_ADDRESS, response.payload, constants.COOKIE_EXPIRATION_DAYS)

    //update table
    updateAlreadyVotedCol();
  }
  else if( response.type == constants.JSON_RPC_RESPONSE)
  {
    $('#poll-modal').modal("hide");

    //fetch new data and update data
    setTimeout(function(){
      _instance.requestScoreReadMethod("exportPolls", {})
      .then(storePolls)
      .then(updateAlreadyVotedCol)
    }, 4000);



  }
}
