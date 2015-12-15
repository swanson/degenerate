from flask import Flask
app = Flask(__name__)

from degenerate import PlayerPool
from degenerate import Optimizer
from degenerate import RosterDefinition

NUMBER_OF_LINEUPS = 3
UNIQUE_PLAYERS = 8

@app.route("/")
def index():
  response = ""

  player_pool = PlayerPool()
  all_players = player_pool.from_csv('projections/cfb_week11_late.csv')
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
    roster = optimizer.generate_roster(all_players, roster_definition, \
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