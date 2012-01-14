$(document).ready(function(){
  var path = location.pathname;
  if(path == "/"){
    $("#home-link").addClass("active");
  } else if(path == "/about/"){
    $("#about-link").addClass("active");
  } else if(path == "/feedback/"){
    $("#feedback-link").addClass("active");
  }

  $('.tabs').tabs();
});

