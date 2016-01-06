from flask import Flask, jsonify
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

from degenerate import PlayerPool
from degenerate import Optimizer
from degenerate import RosterDefinition

NUMBER_OF_LINEUPS = 3
UNIQUE_PLAYERS = 8

player_pool = PlayerPool().from_csv('projections/cfb_week11_late.csv')

@app.route("/player-pool")
def get_player_pool():
  return jsonify({"players": player_pool.as_json()})

@app.route("/")
def index():
  response = ""
  roster_definition = RosterDefinition.DK_CFB

  rosters = []
  optimizer = Optimizer()

  response += "Banned:\n"
  for player in player_pool.banned_players():
    response += str(player) + "\n"

  response += "\n\nLocked:\n"
  for player in player_pool.locked_players():
    response += str(player) + "\n"
  response += "\n<hr>\n"

  for i in range(0, NUMBER_OF_LINEUPS):
    roster = optimizer.generate_roster(player_pool.all_players(), \
                                      roster_definition, \
                                      rosters, UNIQUE_PLAYERS)
    
    if roster is None:
      return "Couldn't generate enough rosters :("
    else: 
      rosters.append(roster)

    response += "\t\tRoster #%s\n" % (i + 1)
    response += str(roster)
    response += "\n\n"

  return response.replace('\n', '<br />')

if __name__ == "__main__":
  app.debug = True
  app.run()