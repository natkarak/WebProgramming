function showLogin(){
  var loginSec = document.getElementById('loginSection');
  if (loginSec.style.display == 'none'){
    loginSec.style.display = '';
  } else {
    loginSec.style.display = 'none';
  }
}   

//dashboard accordion
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
  }
}

                                