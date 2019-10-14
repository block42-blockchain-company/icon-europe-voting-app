export default class Toast
{
  constructor(msg, autohide = true, delay = 3000)
  {
    let toast = this.createToastBody(msg, autohide, delay);
    document.getElementsByTagName("body")[0].appendChild(toast);

    $('.toast').toast('show');
  }

  /* 🤮*/
  createToastBody(message, autohide, delay)
  {
    let toast_container = document.createElement("div");
    toast_container.setAttribute("aria-live", "polite");
    toast_container.setAttribute("aria-atomic", "true");

    let toast_main = document.createElement("div");
    toast_main.setAttribute("class", "toast");
    toast_main.setAttribute("data-delay", "3000");
    toast_main.setAttribute("data-autohide", "true");

    let toast_body = document.createElement("div");
    toast_body.setAttribute("class", "toast-body")

    if(!autohide)
    {
      toast_main.setAttribute("data-autohide", "false");

      let close_button = document.createElement("button");
      close_button.setAttribute("type", "button");
      close_button.setAttribute("class", "ml-2 mb-1 close");
      close_button.setAttribute("data-dismiss", "toast");
      close_button.setAttribute("arisa-label", "Close");

      let x_symbol = document.createElement("span");
      x_symbol.setAttribute("aria-hidden", "true");
      x_symbol.appendChild(document.createTextNode('x'))

      close_button.appendChild(x_symbol);
      toast_body.appendChild(close_button);
    }

    toast_body.appendChild(document.createTextNode(message))
    toast_main.appendChild(toast_body);
    toast_container.appendChild(toast_main);

    return toast_container
  }
}
