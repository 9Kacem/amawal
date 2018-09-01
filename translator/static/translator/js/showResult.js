$(document).ready(function(){
  $("#searchButton").click(function(){
    var inputValue = $("#inputValue").val();

    $.ajax({
      url: '/translate/',
      data: {
        s: inputValue
      },
      dataType: 'json',
      success: function (data) {
          alert(data.inArabic);
      }
    });

  });

});
