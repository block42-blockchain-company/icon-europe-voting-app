import {config} from './config/config.js';

//score_address
export const SCORE_ADDRESS = "cx1ed1f96cc391ad3a95ee07b82572a53287071a44"
export const TEST_SCORE_ADDRESS = config.test_score_address;

// URLS
export const NETWROK_URL = config.url;

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

//CHARTSJS
export const CHART_COLORS = [ "rgb(255, 99, 132)", // red
                                   "rgb(255, 205, 86)", //yellow
                                   "rgb(255, 159, 64)", //orange
                                   "rgb(153, 102, 255)",//purple
                                   "rgb(54, 162, 235)", //blue
                                   "rgb(75, 192, 192)", //green
                                   "rgb(201, 203, 207)"] //grey
