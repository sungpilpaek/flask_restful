$(document).ready(function(){
   $("#submit").click(function(){
      $.ajax({
            type : "POST",
            url : $(this).attr("url_for"),
            data: {"username": $("#username").val()},
            success: function(result) {
                $("#username").val("");
            },
            error: function(request,status,error){
                response_json = JSON.parse(request.responseText);
                alert(error + ":" + response_json["message"]);
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

function showNotification() {
    var popup = document.getElementById("myPopup");
    popup.className = 'popuptext';
    popup.classList.toggle("show");
    setTimeout(function(){
        popup.className = 'hide';
        popup.textContent = '';
    }, 2000);
}

function _display_time() {
    setTimeout('display_time()', 1000)
}

function _get_local_time() {
    const timezone = moment.tz.guess();
    const _format    = "DD MMMM YYYY HH:mm:ss";
    const currentTime = moment().tz(timezone).format(_format);

    return currentTime;
}

function display_time() {
    currentTime = _get_local_time();
    document.getElementById('time').innerHTML = currentTime;
    tt = _display_time();
}

var _data = new Array();
var _source = new EventSource($("#event_stream").attr("url_for"));

_source.addEventListener("notify", function(event) {
   _tmp = JSON.parse(event.data);

   for(i=0; i < _tmp.length; i++) {
      _data.push(_tmp[i]);
      createReminder(_tmp[i]["username"], _tmp[i]["username"])
   }
}, false);

_source.onerror = function(event){
    var txt;
    switch( event.target.readyState ){
       case EventSource.CONNECTING:
           txt = 'Reconnecting to event stream...';
           break;
    }
    console.log(txt);
};

function makeCorsRequest(mode) {
    var json_data = _data

    if (mode == 'one') {
        json_data = _data.shift();
    }

    $.ajax({
        type: 'POST',
        url: 'http://192.168.0.3:5000/api/v1/cors',
        contentType: "application/json",
        data: JSON.stringify({"json": json_data}),
        xhrFields: {
          withCredentials: true
        },
        success: function(result) {
            $.ajax({
                type: 'PATCH',
                url: $("#submit").attr("url_for"),
                contentType: "application/json",
                data: JSON.stringify({
                    "json": json_data,
                    "transferred": true
                }),
                success: function(result) {
                    if (mode == 'one') {
                        remove_item(json_data["username"]);
                    }
                    else {
                        for (i=0; i<json_data.length; i++) {
                            remove_item(json_data[i]["username"]);
                        }
                        _data = new Array();
                    }
                },
                error: function(request,status,error){
                    response_json = JSON.parse(request.responseText);
                    alert(error + ":" + response_json["message"]);
                }
            });
        },
        error: function(request,status,error){
            alert("ERROR");
        }
    });
}

var createReminder = function(id, content, index){
  var reminder = '<li id="' + id + '">' + content + '</li>',
      list = $('.reminders li');
      
  
  if(!$('#'+ id).length){
    
    if(index && index < list.length){
      var i = index +1;
      reminder = $(reminder).addClass('restored-item');
      $('.reminders li:nth-child(' + i + ')').before(reminder);
    }
    if(index === 0){
      reminder = $(reminder).addClass('restored-item');
      $('.reminders').prepend(reminder);
    }
    if(index === list.length){
      reminder = $(reminder).addClass('restored-item');
      $('.reminders').append(reminder);
    }
    if(index === undefined){
      reminder = $(reminder).addClass('new-item');
      $('.reminders').append(reminder); 
    }
  }
};

function remove_item(id) {
   var item = $('#' + id );
   item.addClass('removed-item')
      .one('webkitAnimationEnd oanimationend msAnimationEnd animationend', function(e) {
         $(this).remove();
      });
}