document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('#edit-btn').forEach(btn => {
        btn.onclick = () => display_edit(btn.dataset.id)
    })

    document.querySelectorAll('#delete-plan').forEach(btn => {
        btn.onclick = ()=> {
            document.querySelector('#remove-form').action = `/remove-plan/${btn.dataset.id}`
        }
    })
})


function display_edit(id){

    //hide all the edit buttons when in edit mode

    const element = document.querySelectorAll('#edit-btn')
    for(let i=0; i<element.length; i++){
        element[i].style.display = 'none'
    }


    const old_price = document.querySelector(`#price-${id}`).innerHTML

    document.querySelector(`#price-${id}`).innerHTML = `
    <form id="edit-form-${id}" onsubmit="return false">
    <div class="form-group">
        <input class="form-control" id="new-price-${id}" value = "${old_price}" type="number">
    </div>
    <button type="submit" class="btn btn-primary btn-sm" >Edit</button>
    </form>
    `
    document.querySelector(`#edit-form-${id}`).addEventListener('submit',()=>edit_price(id))
}


function edit_price(id){
    const new_price = document.querySelector(`#new-price-${id}`).value
    

    let csrftoken = getCookie('csrftoken');

    fetch('/edit-price', {
        method: 'POST',
        body: JSON.stringify({
          id: id,
          new_price : new_price
        }),
        headers: { "X-CSRFToken": csrftoken },
    
      })
      
      document.querySelector(`#price-${id}`).innerHTML = new_price

      const element = document.querySelectorAll('#edit-btn')
      for(let i=0; i<element.length; i++){
          element[i].style.display = 'block'
      }
  
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