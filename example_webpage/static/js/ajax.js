$(document).ready(function(){
   $('#submit').click(function(){
      $.ajax({
            type : "POST",
            url : "/transaction",
            data: JSON.stringify({"username": $('#username').val()}),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
               console.log(result);
            }
      });
   })
});