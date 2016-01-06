import React from "react"
import ReactDOM from "react-dom"
import PlayerPool from "./components/playerPool"

import API from "./util/api"

import "./styles/app.scss"

API.getPlayerPool(function(players) {
  ReactDOM.render(
    <PlayerPool players={players}/>,
    document.getElementById("root")
  )
})