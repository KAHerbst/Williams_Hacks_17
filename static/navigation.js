var open=false;

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    open=true;
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    open=false;
}

function testTrue(){
    if (open == true){
      closeNav();
    }
    else if (open == false){
      openNav();
    }
}

$('#menu').on('click', testTrue);
