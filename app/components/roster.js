import React from "react"
import RosterRow from "./rosterRow"

export default React.createClass({
  render() {
    return (
      <div className="roster">
        {this.props.players.map((player, i) => {
          return <RosterRow player={player} key={i}/>
        })}
        <div className="stats">
          <span className="cost">${this.props.cost}</span>
          <span className="projected">{this.props.projected}</span>
        </div>
      </div>
    )
  }
})