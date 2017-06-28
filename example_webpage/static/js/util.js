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
            }
      });
   })

   $(function() {
       $("#username").keypress(function (e) {
           if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
               $('#submit').click();
               return false;
           } else {
               return true;
           }
       });
   });
});