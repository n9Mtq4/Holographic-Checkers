(function() {
    
    var logging = true;
    
    var connect = function(url, messageCallback) {
        
        var ws = new WebSocket(url);
        
        ws.onopen = function() {
            // when the websocket opens
            logln("Opened");
        };
        
        ws.onmessage = function (ev) {
            // when the websocket receives a message from the server
            console.log(ev);
            logln("Message: " + ev.data);
            messageCallback();
        };
        
        ws.onclose = function (ev) {
            // when the websocket closes
            logln("Close: " + ev);
            console.log(ev);
        };
        
        ws.onerror = function (ev) { 
            // when there is an error
            logln("Error: " + ev);
        };
        
        return ws;
        
    };
    
    var log = function(msg) {
        if (!logging) return;
        $('#log').append(msg);
    };
    
    var logln = function(msg) {
        if (!logging) return;
        log(msg + "<br>");
    };
    
    // export
    window.connect = connect;
    window.log = log;
    window.logln = logln;
    
})();
