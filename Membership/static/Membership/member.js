document.addEventListener('DOMContentLoaded', ()=>{
   const element = document.querySelector('#edit-member')
   element.addEventListener('click',()=>{
    display_edit(element.dataset.id)
   })
})


function display_edit(id){

    const email = document.querySelector('#member-email').innerHTML
    const phone = document.querySelector('#member-phone').innerHTML
    const age = document.querySelector('#member-age').innerHTML
    const address = document.querySelector('#member-address').innerHTML

    document.querySelector('#card-profile').style.display = 'none'

    document.querySelector('#member-details').innerHTML = 
    `<form action="" id="edit-form" onsubmit="return false">
      
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

document.querySelector('#edit-form').addEventListener('submit', ()=>editMember(id))

}


function editMember(id){

    let csrftoken = getCookie('csrftoken');

    const email = document.querySelector('#member-email').value
    const phone = document.querySelector('#member-phone').value
    const age = document.querySelector('#member-age').value
    const address = document.querySelector('#member-address').value

    fetch('/edit',{
        method: 'POST',
        body: JSON.stringify({
            id: id,
            email:email,
            phone:phone,
            age:age,
            address:address,
        }),
        headers: { "X-CSRFToken": csrftoken },

    })
    window.location.replace(`${id}`);
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