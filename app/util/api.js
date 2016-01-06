var request = new XMLHttpRequest()

export default {
  getPlayerPool: function(cb) {
    request.open('GET', 'http://localhost:5000/player-pool', true)
    request.onload = function() {
      cb(JSON.parse(request.responseText).players)
    }
    request.send()
  }
}