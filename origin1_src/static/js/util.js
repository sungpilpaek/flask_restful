$(document).ready(function(){
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

var _source = new EventSource($("#event_stream").attr("url_for"));

_source.addEventListener("notify", function(event) {
   _tmp = event.data;

   for(i=0; i < _tmp.length; i++) {
      createReminder(_tmp, _tmp)
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
  setTimeout(function(){
      remove_item(id);
  }, 2000);
};

function remove_item(id) {
   var item = $('#' + id );
   item.addClass('removed-item')
      .one('webkitAnimationEnd oanimationend msAnimationEnd animationend', function(e) {
         $(this).remove();
      });
}