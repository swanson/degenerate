import React from "react"
import ReactDOM from "react-dom"
import Optimizer from "./components/optimizer"

import "./styles/app.scss"

import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

ReactDOM.render(
  <Optimizer/>,
  document.getElementById("root")
)