class Poll
{
  constructor( poll_info )
  {
    this.id = parseInt(poll_info.id);
    this.name = poll_info.name;
    this.question = poll_info.question;
    this.start_date = poll_info.start_date;
    this.end_date = poll_info.end_date;
    this.description = poll_info.description;
    this.candidates = poll_info.candidates;
  }

  render()
  {
    let tbody = document.getElementById("polls-table").getElementsByTagName("tbody")[0];
    let row = tbody.insertRow();

    row.setAttribute("id", "poll-" + this.id);

    for( var key in this)
    {
      if( key == "name")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "start_date")
        row.insertCell().appendChild(document.createTextNode(this[key]));
      else if ( key == "end_date")
        row.insertCell().appendChild(document.createTextNode(this[key]));
    }

    row.addEventListener( "click", this.openDetailView);

  }

  openDetailView()
  {
      let poll = getPollByID( parseInt(this.id.split("-")[1])) //split id from string --> maybe write function to this???!?

      document.getElementsByClassName("poll-title")[0].innerHTML = poll.name;
      document.getElementsByClassName("poll-question")[0].innerHTML = poll.question;



      $('#poll-modal').modal("toggle");


  }
}
