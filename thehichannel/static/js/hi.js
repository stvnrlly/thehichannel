// When we're using HTTPS, use WSS too.
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host);

// What to do when a message comes through the websocket
socket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    var hilist = $("#hi-list");
    var block = $('<blockquote></blockquote').text(data.hi);
    var sender = $('<a>', {text: data.sender, href: '/user/'+data.sender});
    var note = $('<small></small>').text(', '+data.timestamp).prepend(sender);
    block.append(note);
    hilist.prepend(block);
};

// When the socket opens
// socket.onopen = function() {
//   console.log('socket open!');
// };

// Logic for the form submission
$("#hiform").on("submit", function(event) {
    var message = {
        sender: {{ user.id }},
        message: $('#message').val(),
    };
    socket.send(JSON.stringify(message));
    $("#message").val('').focus();
    return false;
});
