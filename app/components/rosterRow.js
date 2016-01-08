import React from "react"

export default React.createClass({
  render() {
    return (
      <div className="roster-row">
        <div className="position">{this.props.player.position}</div>
        <div className="name">{this.props.player.name}</div>
        <div className="salary">${this.props.player.salary}</div>
        <div className="projection">{this.props.player.projection}</div>
      </div>
    )
  }
})