(function() {
    
    $(document).ready(function() {
        
        var ws = undefined;
        
        var onmessage = function(ev) {
            // this is called when we get a message from the server
            alert(ev.data);
        };
        
        $('#connect').click(function() {
            
            var ipForm = $('#ip');
            var ip = ipForm.val();
            
            logln("connecting to " + ip);
            ws = connect(ip, onmessage);
            logln("connected to " + ip);
            
        });
        
        $('#send').click(function () {
            
            if (!ws) return; // haven't connected yet
            
            var msgForm = $('#msg');
            var msg = msgForm.val();
            logln("Sending msg: " + msg);
            ws.send(msg);
            
        });
        
    });
    
})();
