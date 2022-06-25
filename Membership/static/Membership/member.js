document.addEventListener('DOMContentLoaded', () => {
  const element = document.querySelector('#edit-member')
  element.addEventListener('click', () => {
    display_edit(element.dataset.id)
  })
  const renew_btn = document.querySelector('#renew')
  renew_btn.addEventListener('click', ()=>{
    display_renew(renew_btn.dataset.id)
  })
})


function display_edit(id) {

  const email = document.querySelector('#member-email').innerHTML
  const phone = document.querySelector('#member-phone').innerHTML
  const age = document.querySelector('#member-age').innerHTML
  const address = document.querySelector('#member-address').innerHTML

  document.querySelector('#head').style.display = 'none'
  document.querySelector('#card-profile').style.display = 'none'

  document.querySelector('#member-details').innerHTML =
    `
    <h2 style="text-align: center;">Edit Member Detail</h2>

    <form action="" id="edit-form" onsubmit="return false">
      
    <div class="row">
      <div class="col-sm-3">
        <p class="mb-0">Email</p>
      </div>
      <div class="col-sm-9">
        <input type="text" value="${email}" class="form-control" id="member-email">
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-sm-3">
        <p class="mb-0">Phone Number</p>
      </div>
      <div class="col-sm-9">
        <input type="text"  value="${phone}" class="form-control" id="member-phone">
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-sm-3">
        <p class="mb-0">Age</p>
      </div>
      <div class="col-sm-9">
        <input type="text"  value="${age}" class="form-control" id="member-age">
      </div>
    </div>
    <hr>
   
    <div class="row">
      <div class="col-sm-3">
        <p class="mb-0">Address</p>
      </div>
      <div class="col-sm-9">
        <input type="text" value="${address}" class="form-control" id="member-address">
      </div>
    </div>
    <hr>
   
    <input type="submit"  value ="Edit" class="btn btn-primary btn-sm">

</form>`
  document.querySelector('#edit-form').addEventListener('submit', () => editMember(id))

}


function editMember(id) {

  let csrftoken = getCookie('csrftoken');

  const email = document.querySelector('#member-email').value
  const phone = document.querySelector('#member-phone').value
  const age = document.querySelector('#member-age').value
  const address = document.querySelector('#member-address').value

  fetch('/edit', {
    method: 'POST',
    body: JSON.stringify({
      id: id,
      email: email,
      phone: phone,
      age: age,
      address: address,
    }),
    headers: { "X-CSRFToken": csrftoken },

  })
  window.location.reload(`${id}`);
}



function display_renew(id) {



  document.querySelector('#head').style.display = 'none'
  document.querySelector('#card-profile').style.display = 'none'

  document.querySelector('#member-details').innerHTML =
    `
    <h2 style="text-align: center;">Renew Membership </h2>

    <form action="" id="renew-form" onsubmit="return false">
      
    <div class="row">
      <div class="col-sm-3">
        <p class="mb-0">Valid Until</p>
      </div>
      <div class="col-sm-9">
        <input type="date"  class="form-control" id="valid-date">
      </div>
    </div>
 
   
   
    <input type="submit"  value ="Renew" class="btn btn-primary btn-sm">

</form>`

  document.querySelector('#renew-form').addEventListener('submit', () => renew(id))

}


function renew(id){

  let csrftoken = getCookie('csrftoken');


  const date = document.querySelector('#valid-date').value

  fetch('/renew', {
    method: 'POST',
    body: JSON.stringify({
      id: id,
      date:date
    }),
    headers: { "X-CSRFToken": csrftoken },

  })
  window.location.reload(`${id}`);
}


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}