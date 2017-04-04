var exampleSocket = new WebSocket("ws://localhost:8765");

exampleSocket.onmessage = function (event) {
  vm.text(event.data)
}

exampleSocket.onopen = function () {
  vm.text("Connected to the server!")
}

function sendText(msg) {
  exampleSocket.send(msg);
}

var vm = {
  text: ko.observable("Hello, connecting to server")
}

ko.applyBindings(vm)
