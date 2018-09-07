$(document).ready(function(){
  $("#searchForm").submit(function(e){
    var form = $(this);
    var ul = $("#resultsContainer ul");
    var ara = $("#arabicSpan");
    var fr  = $("#frenchSpan");

    $.ajax({
      type: "GET",
      url: form.attr('action'),
      data: form.serialize(),
      dataType: 'json',

      success: function (data) {

          ul.show();
          ara.html("");
          fr.html("");

          if (JSON.stringify(data) === JSON.stringify({})) {
            ara.append("Word does not exist")
            fr.append("Word does not exist")
          } else {
            ara.append(data.inArabic);
            fr.append(data.inFrench);
          }
      }

    }); // ajax end

    e.preventDefault(); // stops the default submit button

  }); // searchForm.submit end
}); //document.ready end
