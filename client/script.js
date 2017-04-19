var exampleSocket = new WebSocket("ws://localhost:8765");

exampleSocket.onmessage = function (event) {
  try {
    var o = JSON.parse(event.data)
  } catch(e) {
    var o = {}
    o.text = event.data
    o.type = "text"
  }
  console.log("got message", o)

  switch (o.type) {
    case "command":
      switch(o.command) {
        case "active-mode": vm.mode("active"); break;
        case "passive-mode": vm.mode("passive"); break;
      }
      break;
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
      vm.json(JSON.stringify(o.json, null, 2))
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
  news: ko.observableArray([]),
  mode: ko.observable("passive")
}

ko.applyBindings(vm)
