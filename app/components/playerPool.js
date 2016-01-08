import React from "react"
import API from "../util/api"

export default React.createClass({
  getInitialState: function() {
    return {
      rosters: []
    }
  },

  render: function() {
    var rows = []
    var rosterRows = []

    this.props.players.forEach(function(player) {
      rows.push(
        <tr key={player.name}>
          <td>{player.position}</td>
          <td>{player.name}</td>
          <td>${player.salary}</td>
          <td>{player.projection}</td>
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