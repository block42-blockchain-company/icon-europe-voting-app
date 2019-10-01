export default class Toast
{
  constructor(message)
  {
    document.getElementsByClassName("toast-body")[0].innerHTML = message;
    $('.toast').toast('show');
  }
}
