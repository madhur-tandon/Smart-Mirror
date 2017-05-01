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
    case "weather":
      vm.type("weather")
      vm.weather.intent(o.intent)
      vm.weather.location(o.location? o.location: "")
      vm.weather.data(o.data instanceof Array? o.data : [o.data])
      console.log("completed without error")
      break;
    case "tic-tac-toe":
      vm.type("tic-tac-toe")
      vm.ticTacToe(o.data)
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
  mode: ko.observable("passive"),
  weather: {
    intent: ko.observable(""),
    location: ko.observable(""),
    data: ko.observableArray([{
      tempMin: 1,
      tempMax: 1,
      summary: "Ko breaks without this",
      icon: "",
      humidity: "",
      pressure: ""
    },
    {
      tempMin: 1,
      tempMax: 1,
      summary: "Ko breaks without this",
      icon: ""
    },
    {
      tempMin: 1,
      tempMax: 1,
      summary: "Ko breaks without this",
      icon: ""
    }])
  },
  ticTacToe: ko.observableArray(["", "", "", "", "", "", "", "", ""])
}

ko.applyBindings(vm)
