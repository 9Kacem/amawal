for (i = 65; i < 99; i++) {
  var tmpVal =   $("#div1").text();
  var str =String.fromCharCode(i);
  $("#div1").text(tmpVal+" "+str);
}
