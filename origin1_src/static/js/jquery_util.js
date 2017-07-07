$(document).ready(function(){
   $("#submit").click(function(){
      $.ajax({
            type : "POST",
            url : $(this).attr("url_for"),
            data: {"username": $("#username").val()},
            success: function(result) {
               showNotification();
               $("#myPopup").html($("#username").val() + " is now connected!");
               $("#username").val("");
            },
            error: function(request,status,error){
               console.log("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
            }
      });
   });

   $("#username").keypress(function (e) {
       if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
           $("#submit").click();
           return false;
       } else {
           return true;
       }
   });

   display_time();
});