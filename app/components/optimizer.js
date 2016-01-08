import React from "react"
import API from "../util/api"
import PlayerPool from "./playerPool"
import RosterGrid from "./rosterGrid"

export default React.createClass({
  getInitialState() {
    return {
      players: [],
      rosters: []
    }
  },

  componentWillMount() {
    API.getPlayerPool(players => {
      this.setState({ players: players })
    })
  },

  optimize() {
    API.optimize(this.state.players, rosters => {
      this.setState({ rosters: rosters })
    })
  },

  toggleLock(target) {
    var players = this.state.players.map(player => {
      if (target === player) {
        player.locked = !player.locked
        player.banned = false
      }
      return player
    })

    this.setState({players: players})
  },

  toggleBan(target) {
    var players = this.state.players.map(player => {
      if (target === player) {
        player.banned = !player.banned
        player.locked = false
      }
      return player
    })

    this.setState({players: players})
  },

  render() {
    return (
      <div>
        <div className="header">
          <h1>Optimizer</h1>
          <button onClick={this.optimize}>Optimize</button>
        </div>
        <div className="content">
          <PlayerPool players={this.state.players} 
            onLock={this.toggleLock}
            onBan={this.toggleBan}/>
          <RosterGrid rosters={this.state.rosters} />
        </div>
      </div>
    )
  }
})