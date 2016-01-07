from flask import Flask, jsonify, request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

from degenerate import PlayerPool
from degenerate import Optimizer
from degenerate import RosterDefinition

NUMBER_OF_LINEUPS = 3
UNIQUE_PLAYERS = 8

player_pool = PlayerPool().from_csv('projections/cfb_week11_late.csv')
optimizer = Optimizer()

roster_definition = RosterDefinition.DK_CFB

@app.route("/player-pool")
def get_player_pool():
  return jsonify({"players": player_pool.as_json()})

@app.route("/optimize", methods=['POST'])
def post_optimize():
  content = request.get_json()
  pool = PlayerPool().from_json(content)

  rosters = []
  for i in range(0, 3):
    rosters.append(optimizer.generate_roster(pool.all_players(), \
                                          roster_definition, \
                                          rosters, UNIQUE_PLAYERS))

  return jsonify({"rosters": map(lambda x: x.__json__(), rosters)})

if __name__ == "__main__":
  app.debug = True
  app.run()