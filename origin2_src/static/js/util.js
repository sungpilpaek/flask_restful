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

function access_time(){
    currentTime = _get_local_time();
    document.getElementById('access_log').value = currentTime;
}

// Create the XHR object.
function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        // XHR for Chrome/Firefox/Opera/Safari.
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        // XDomainRequest for IE.
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        // CORS not supported.
        xhr = null;
    }
    return xhr;
}

// Make the actual CORS request.
function makeCorsRequest1() {
    // This is a sample server that supports CORS.
    var url = '192.168..';

    var xhr = createCORSRequest('GET', url);
    if (!xhr) {
        alert('CORS not supported');
        return;
    }

    // Response handlers.
    xhr.onload = function() {
        var text = xhr.responseText;
        alert('Response from CORS request to ' + url + ': ' + text);
    };

    xhr.onerror = function() {
        alert('Woops, there was an error making the request.');
    };

    xhr.send();
}

// Make the actual CORS request.
function makeCorsRequest2() {
    // This is a sample server that supports CORS.
    var url = '192.168..';

    var xhr = createCORSRequest('POST', url);
    if (!xhr) {
        alert('CORS not supported');
        return;
    }

    // Response handlers.
    xhr.onload = function() {
        var text = xhr.responseText;
        alert('Response from CORS request to ' + url + ': ' + text);
    };

    xhr.onerror = function() {
        alert('Woops, there was an error making the request.');
    };

    xhr.send();
}