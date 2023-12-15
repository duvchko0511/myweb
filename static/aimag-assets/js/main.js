
//////////////////////  CheckPage  ////////////////////////
var CPonSuccess = function(response) {
    var errorDivs = document.getElementsByClassName("hcaptcha-error");
    if (errorDivs.length) {
      errorDivs[0].className = "";
    }
    var errorMsgs = document.getElementsByClassName("hcaptcha-error-message");
    if (errorMsgs.length) {
      errorMsgs[0].parentNode.removeChild(errorMsgs[0]);
    }

    var logEl = document.querySelector(".hcaptcha-success");
    logEl.innerHTML = "Challenge Success!"
    if (logEl.innerHTML = "Challenge Success!"){
      document.querySelector("#hcaptcha-demo-submit").disabled = false;
    }
    
  };

  var CPonExpire = function(response) {
    var logEl = document.querySelector(".hcaptcha-success");
    logEl.innerHTML = "Token expired."
  };
      // beacon example
      function CPaddEventHandler(object,szEvent,cbCallback){
        if(!!object.addEventListener){ // for modern browsers or IE9+
            return object.addEventListener(szEvent,cbCallback);
        }
        if(!!object.attachEvent){ // for IE <=8
            return object.attachEvent(szEvent,cbCallback);
        }
        };
        // Ex: triggers pageview beacon
        CPaddEventHandler(window,'load',function(){b();});
        // Ex: triggers event beacon without pageview
        CPaddEventHandler(window,'load',function(){b({"vt": "e", "ec": "test_cat", "ea": "test_action"});});
        

/////////////////  ForgetPassword  ///////////////////


////////////////////////  UserDashBoard  ///////////////////////
$(".menu").click(function () {
  $("#mySidenav").css("width", "70px");
  $("#main").css("margin-left", "70px");
  $(".logo").css("display", "none");
  $(".logo1").css("display", "block");
  $(".logo span").css("visibility", "visible");
  $(".logo span").css("margin-left", "-10px");
  $(".icon-a").css("visibility", "hidden");
  $(".icon-a").css("height", "25px");
  $(".icons").css("visibility", "visible");
  $(".icons").css("margin-left", "-8px");
  $(".menu1").css("display", "block");
  $(".menu").css("display", "none");
});

$(".menu1").click(function () {
  $("#mySidenav").css("width", "300px");
  $("#main").css("margin-left", "300px");
  $(".logo").css("visibility", "visible");
  $(".logo").css("display", "block");
  $(".icon-a").css("visibility", "visible");
  $(".icons").css("visibility", "visible");
  $(".menu").css("display", "block");
  $(".menu1").css("display", "none");
});

$(document).ready(function () {
  $(".profile p").click(function () {
    $(".profile-div").toggle();
  });
});

function UDBopenNav() {
a=document.getElementById("mySidepanel");
b=document.getElementById("huselt");
c=document.getElementById("oyutan");
if (a.style.width ==="150px"){
a.style.width = "0";
}
else {
a.style.width = "150px"
b.style.width = "0"
c.style.width = "0"
}
}
function UDBcloseNav() {
document.getElementById("mySidepanel").style.width = "0";
}

function UDBopenN() {
a=document.getElementById("huselt");
b=document.getElementById("mySidepanel");
c=document.getElementById("oyutan");

if (a.style.width ==="150px" ){
a.style.width = "0";
}
else {
a.style.width = "150px"
b.style.width = "0"
c.style.width = "0"
}
}
function UDBcloseN() {
document.getElementById("huselt").style.width = "0";
}
function UDBopens() {
document.getElementById("me").style.width = "150px";
}
function UDBcloses() {
document.getElementById("me").style.width = "0";
}
//hvselt

function UDBopenN3() {
a=document.getElementById("mySidepanel");
b=document.getElementById("huselt");
c=document.getElementById("oyutan");
if (c.style.width ==="150px"){
  c.style.width = "0";
}
else {
  a.style.width = "0"
  b.style.width = "0"
  c.style.width = "150px"
}
}
function UDBcloseN3() {
document.getElementById("oyutan").style.width = "0";
}

    
//////////////////////  TUserLlist  //////////////////////
function ULmyFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
  let a = document.getElementsByTagName("tr").length;
  let i = 1;
  let b = 0;
  while (i < a) {
    document.getElementsByClassName("asd")[b].innerHTML = i;
    b += 1;
    i += 1;
  }
