$(document).ready(function(){
  $("#searchForm").submit(function(e){
    var form = $(this);

    $.ajax({
      type: "GET",
      url: form.attr('action'),
      data: form.serialize(),
      dataType: 'json',
      success: function (response) {
          alert(response.inArabic);
      }
    });

    e.preventDefault(); // stops the default submit button

  });

});

// TODO: change alert to good front-end
