$(document).ready(function(){
   $('#submit').click(function(){
      $.ajax({
            type : "POST",
            url : "/transaction",
            data: JSON.stringify({"username": $('#username').val()}),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
               showNotification();
               $('#myPopup').html(result + " is now connected!");
               $('#username').val('');
               console.log(result);
            }
      });
   })
});