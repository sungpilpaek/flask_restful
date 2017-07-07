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