import React from "react"
import API from "../util/api"
import classNames from "classNames"

import Card from 'material-ui/lib/card/card';
import CardHeader from 'material-ui/lib/card/card-header';
import CardText from 'material-ui/lib/card/card-text';

import Table from 'material-ui/lib/table/table';
import TableBody from 'material-ui/lib/table/table-body';
import TableFooter from 'material-ui/lib/table/table-footer';
import TableHeader from 'material-ui/lib/table/table-header';
import TableHeaderColumn from 'material-ui/lib/table/table-header-column';
import TableRow from 'material-ui/lib/table/table-row';
import TableRowColumn from 'material-ui/lib/table/table-row-column';

import ActionLock from 'material-ui/lib/svg-icons/action/lock';
import ActionLockOpen from 'material-ui/lib/svg-icons/action/lock-open';
import RemoveCircle from 'material-ui/lib/svg-icons/content/remove-circle';
import RemoveCircleOutline from 'material-ui/lib/svg-icons/content/remove-circle-outline';
import Colors from 'material-ui/lib/styles/colors';

export default React.createClass({
  getInitialState() {
    return {
      rosters: []
    }
  },

  lock(player) {
    this.props.onLock(player)
  },

  ban(player) {
    this.props.onBan(player)
  },

  render() {
    var rows = []

    this.props.players.forEach((player) => {
      rows.push(
        <TableRow key={player.name}>
          <TableRowColumn>{player.position}</TableRowColumn>
          <TableRowColumn>{player.name}</TableRowColumn>
          <TableRowColumn>{player.salary}</TableRowColumn>
          <TableRowColumn>{player.projection}</TableRowColumn>
          <TableRowColumn>
            <span onClick={this.lock.bind(this, player)}>
              {player.locked ? <ActionLock color={Colors.yellowA700}/> : <ActionLockOpen />}
            </span>
          </TableRowColumn>
          <TableRowColumn>
            <span onClick={this.ban.bind(this, player)}>
              {player.banned ? <RemoveCircle color={Colors.deepOrangeA700}/> : <RemoveCircleOutline />}
            </span>
          </TableRowColumn>
        </TableRow>
      )
    })
    
    return (
      <Card initiallyExpanded={true}>
        <CardHeader title="Player Pool"
          subtitle="Pick your team" 
          actAsExpander={true} 
          showExpandableButton={true} />
        <CardText expandable={true}>
          <Table height="400px"
            selectable={false}>
            <TableHeader displaySelectAll={false}>
              <TableRow>
                <TableHeaderColumn>Position</TableHeaderColumn>
                <TableHeaderColumn>Player</TableHeaderColumn>
                <TableHeaderColumn>Salary</TableHeaderColumn>
                <TableHeaderColumn>Projection</TableHeaderColumn>
                <TableHeaderColumn>Lock</TableHeaderColumn>
                <TableHeaderColumn>Ban</TableHeaderColumn>
              </TableRow>
            </TableHeader>
            <TableBody showRowHover={true}
              stripedRows={true}>
              {rows}
            </TableBody>
          </Table>
        </CardText>
      </Card>
    )
  }
})