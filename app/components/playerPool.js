import React from "react"
import API from "../util/api"

export default React.createClass({
  getInitialState: function() {
    return {
      rosters: []
    }
  },

  optimize: function() {
    var that = this

    API.optimize(this.props.players, function(rosters) {
      that.setState({
        rosters: rosters
      })
    })
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

    this.state.rosters.forEach(function(roster, i) {
      roster.players.forEach(function(player, j) {
        rosterRows.push(
          <tr key={i + "-" + j + "-" + player.name}>
            <td>{player.position}</td>
            <td>{player.name}</td>
            <td>${player.salary}</td>
            <td>{player.projection}</td>
          </tr>
        )
      })

      rosterRows.push(
        <tr key={"roster-" + i}>
          <td>{roster.cost}</td>
          <td>{roster.projected}</td>
        </tr>
      )
    })
    
    return (
      <div>
        <button onClick={this.optimize}>Optimize</button>
        <table className="player-pool">
         <tbody>
          {rows}
         </tbody>
        </table>

        <table className="rosters">
         <tbody>
          {rosterRows}
         </tbody>
        </table>
      </div>
    )
  }
})