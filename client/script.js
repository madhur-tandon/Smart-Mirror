var exampleSocket = new WebSocket("ws://localhost:8765");

exampleSocket.onmessage = function (event) {
  try {
    var o = JSON.parse(event.data)
  } catch(e) {
    var o = {}
    o.text = event.data
    o.type = "text"
  }
  
  switch (o.type) {
    case "image":
      vm.type("image")
      vm.imageSrc(o.src)
      break;
    case "text":
      vm.type("text")
      vm.text(o.text)
      break;
    case "json":
      vm.type("json")
      vm.json(o.json)
      break;
    case "news":
      vm.type("news")
      vm.news(ko.mapping.fromJS(o.items)())
      break;
  }
}

exampleSocket.onopen = function () {
  vm.text("Connected to the server!")
}

function sendText(msg) {
  exampleSocket.send(msg);
}

var vm = {
  text: ko.observable("Hello, connecting to server"),
  type: ko.observable("text"),
  json: ko.observable("{}"),
  imageSrc: ko.observable(""),
  news: ko.observableArray([])
}

ko.applyBindings(vm)