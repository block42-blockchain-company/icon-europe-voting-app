const iconService = window['icon-sdk-js'];
// const httpProvider = new iconService(new iconService.HttpProvider('https://bicon.net.solidwallet.io/api/v3'))
const httpProvider = new iconService(new iconService.HttpProvider('http://127.0.0.1:9000/api/v3'))
const iconAmount = iconService.IconAmount;
const iconConverter = iconService.IconConverter;
const iconBuilder = iconService.IconBuilder;

class ScoreHandler
{

  constructor(keystore, password, score_address)
  {
    this._wallet = iconService.IconWallet.loadKeystore(keystore, password);
    this._score_address = score_address;
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

  async executeScoreWriteMethod( method, params )
  {

  }
}
