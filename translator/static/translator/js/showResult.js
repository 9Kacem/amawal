$(document).ready(function(){
  $("#searchButton").click(function(){
    var myString = $("#inputField").val();
    $.get("/?s="+myString);
  });
});

function fetchWord(data, status){
    alert("Data: " + data + "\nStatus: " + status);
}
