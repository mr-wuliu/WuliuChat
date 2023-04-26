$(document).ready(function () {
    //Socket.IO start connect
    // var socket = io.connetc();
    namespace = '/chat'
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    // Socket.IO send message
    $("#send").click(function (e) {
        //send message
        socket.emit('send', $('#message').val())
        //clear input filed
        $('#message').val('')
    });
    //Socket.IO get message
    socket.on('get', function (data) {
        $('#chat_content').append('<p>I say: ' + data + '</p>');
    });
    // Socket.IO get test
    socket.on("message", function(data) {
        $('#chat_content').append('<p>System: '+ data + '</p>')
    });
    // Socket.IO send test
    $("#test").click(function (e) {
        socket.emit('test')
    });
});