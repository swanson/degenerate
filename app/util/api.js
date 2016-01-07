var request = new XMLHttpRequest()

export default {
  getPlayerPool: function(cb) {
    request.open('GET', 'http://localhost:5000/player-pool', true)
    request.onload = function() {
      cb(JSON.parse(request.responseText).players)
    }
    request.send()
  },

  optimize: function(data, cb) {
    var request = new XMLHttpRequest()
    request.open('POST', 'http://localhost:5000/optimize', true)
    request.setRequestHeader('Content-Type', 'application/json')
    request.onload = function() {
      cb(JSON.parse(request.responseText).rosters)
    }
    request.send(JSON.stringify(data))
  }
}