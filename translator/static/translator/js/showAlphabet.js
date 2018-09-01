for (i = 65; i < 91; i++) {
  var tmpVal =   $("#Alphabet-Div").html();
  var newLetter = String.fromCharCode(i);
  $("#Alphabet-Div").append("<a href=\"" + newLetter + "\">"+newLetter+"</a>");
}
