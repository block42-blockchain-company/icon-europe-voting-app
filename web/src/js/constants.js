//score_address
export const SCORE_ADDRESS = "cx02716d61c742fa219a5f0e9fa9d98ae56e5a9075"

// URLS
export const TESTNET_URL = 'https://bicon.net.solidwallet.io/api/v3';
export const LOCALHOST_URL = 'http://localhost:9000/api/v3';

//ICONEX wallet responses
export const ICONEX_RESPONSE = "ICONEX_RELAY_RESPONSE"; //Iconex parent response
export const HAS_ACCOUNT_RESPONSE = "RESPONSE_HAS_ACCOUNT"; //iconex has account response
export const ADDRESS_RESPONSE = "RESPONSE_ADDRESS"; //iconex address response
export const JSON_RPC_RESPONSE = "RESPONSE_JSON-RPC"; //iconex address response

//ICONEX wallet requests
export const HAS_ACCOUNT_REQUEST = new CustomEvent( 'ICONEX_RELAY_REQUEST', { detail: {
  type: 'REQUEST_HAS_ACCOUNT'
}});
export const ADDRESS_REQUEST = new CustomEvent( 'ICONEX_RELAY_REQUEST', { detail: {
     type: 'REQUEST_ADDRESS'
}});

//BUTTONS
export const REQUEST_ADDRESS_BUTTON = document.getElementById("btn-wallet");

//Table
export const TABLE = document.getElementById("polls-table");

//MODALS
export const POLL_MODAL = document.getElementById("poll-modal");

// ERROR Messages
export const GET_BY_CLASSNAME_UNDEFINED = "document.getElementsByClassName(...)[0] is undefined";
export const WALLET_UNCONNECTED = "You need to connect to your wallet first.";

//COOKIES
export const COOKIE_NAME_WALLET_ADDRESS = "wallet_address"
export const COOKIE_EXPIRATION_DAYS = 30
