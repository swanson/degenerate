import React from "react"

export default React.createClass({
  render: function() {
    var rows = []

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