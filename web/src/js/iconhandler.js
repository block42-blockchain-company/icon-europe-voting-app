
const iconService = window['icon-sdk-js'];
// const httpProvider = new iconService(new iconService.HttpProvider('https://bicon.net.solidwallet.io/api/v3'))
const httpProvider = new iconService(new iconService.HttpProvider('http://127.0.0.1:9000/api/v3'))
const iconBuilder = iconService.IconBuilder;

//score_address
let score_address = "cx08bed0a6999a6c3f866d26c1be67e3e1139ba75a"

//ICONEX wallet responses
const iconex_response = "ICONEX_RELAY_RESPONSE"; //Iconex parent response
const has_account_response = "RESPONSE_HAS_ACCOUNT"; //iconex has account response
const address_response = "RESPONSE_ADDRESS"; //iconex address response

//ICONEX wallet requests
const has_account_request = new CustomEvent( 'ICONEX_RELAY_REQUEST', { detail: {
  type: 'REQUEST_HAS_ACCOUNT'
}});
const address_request = new CustomEvent( 'ICONEX_RELAY_REQUEST', { detail: {
     type: 'REQUEST_ADDRESS'
}});
//ICONEX wallet request button
const request_address_button = document.getElementsByClassName("btn-wallet")[0];

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
      this._score_address = score_address;

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
  request_address_button.addEventListener("click", requestWallet)

  //catch response
  window.addEventListener(iconex_response, responseWallet, false)

}


function requestWallet()
{
  window.dispatchEvent(has_account_request);
}

function responseWallet(ev)
{
  let response = ev.detail;

  if(response.type == has_account_response)
  {
    if(response.payload.hasAccount)
    window.dispatchEvent(address_request);
  }
  else if ( response.type == address_response )
  {
    _instance._wallet = response.payload;
    request_address_button.innerHTML = response.payload;
    request_address_button.removeEventListener("click", requestWallet);
  }
}
