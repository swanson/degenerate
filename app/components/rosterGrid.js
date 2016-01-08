import React from "react"
import Roster from "./roster"

export default React.createClass({
  render() {
    return (
      <div className="roster-grid">
        {this.props.rosters.map((roster, i) => {
          return <Roster {...roster} key={i} />
        })}
      </div>
    )
  }
})