(function() {
    
    $(document).ready(function() {
        
        var ws = undefined;
        
        $('#connect').click(function() {
            
            var ipForm = $('#ip');
            var ip = ipForm.val();
            
            logln("connecting to " + ip);
            ws = connect(ip);
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
