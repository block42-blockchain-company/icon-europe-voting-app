//score_address
export const SCORE_ADDRESS = "cx08bed0a6999a6c3f866d26c1be67e3e1139ba75a"

//ICONEX wallet responses
export const ICONEX_RESPONSE = "ICONEX_RELAY_RESPONSE"; //Iconex parent response
export const HAS_ACCOUNT_RESPONSE = "RESPONSE_HAS_ACCOUNT"; //iconex has account response
export const ADDRESS_RESPONSE = "RESPONSE_ADDRESS"; //iconex address response

//ICONEX wallet requests
export const HAS_ACCOUNT_REQUEST = new CustomEvent( 'ICONEX_RELAY_REQUEST', { detail: {
  type: 'REQUEST_HAS_ACCOUNT'
}});
export const ADDRESS_REQUEST = new CustomEvent( 'ICONEX_RELAY_REQUEST', { detail: {
     type: 'REQUEST_ADDRESS'
}});
//ICONEX wallet request button
export const REQUEST_ADDRESS_BUTTON = document.getElementById("btn-wallet");

export const VOTE_BUTTON = document.getElementById("btn-vote");

// ERROR Messages
export const GET_BY_CLASSNAME_UNDEFINED = "document.getElementsByClassName(...)[0] is undefined";
export const WALLET_UNCONNECTED = "You need to connect to your wallet first.";
