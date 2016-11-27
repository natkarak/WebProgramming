//dashboard accordion
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
  }
}

//responsible menu for small screens - shows the icon instead of all the tabs
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}


//shows the login form
var modal = document.getElementById('logSec');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}                                