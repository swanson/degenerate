import React from "react"
import API from "../util/api"
import classNames from "classNames"

export default React.createClass({
  getInitialState: function() {
    return {
      rosters: []
    }
  },

  lock: function(player) {
    this.props.onLock(player)
  },

  ban: function(player) {
    this.props.onBan(player)
  },

  render: function() {
    var rows = []
    var rosterRows = []

    this.props.players.forEach((player) => {
      var cssNames = classNames({
        'banned': player.banned,
        'locked': player.locked
      })

      rows.push(
        <tr key={player.name} className={cssNames}>
          <td>{player.position}</td>
          <td>{player.name}</td>
          <td>${player.salary}</td>
          <td>{player.projection}</td>
          <td onClick={this.lock.bind(this, player)}>Lock</td>
          <td onClick={this.ban.bind(this, player)}>Ban</td>
        </tr>
      )
    })
    
    return (
      <table className="player-pool">
       <tbody>
        {rows}
       </tbody>
      </table>
    )
  }
})