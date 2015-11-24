from ortools.linear_solver import pywraplp

import csv

class Player:
  def __init__(self, opts):
    self.name = opts['player']
    self.position = opts['position'].upper()
    self.salary = int(opts['salary'])
    self.projected = float(opts['projection'])
    self.lock = int(opts['lock']) > 0
    self.ban = int(opts['lock']) < 0

  def __repr__(self):
    return "[{0: <2}] {1: <20}(${2}, {3}) {4}".format(self.position, \
                                    self.name, \
                                    self.salary,
                                    self.projected,
                                    "LOCK" if self.lock else "")

class Roster:
  POSITION_ORDER = {
    "QB": 0,
    "RB": 1,
    "WR": 2
  }

  def __init__(self):
    self.players = []

  def add_player(self, player):
    self.players.append(player)

  def spent(self):
    return sum(map(lambda x: x.salary, self.players))

  def projected(self):
    return sum(map(lambda x: x.projected, self.players))

  def position_order(self, player):
    return self.POSITION_ORDER[player.position]

  def sorted_players(self):
    return sorted(self.players, key=self.position_order)

  def __repr__(self):
    s = '\n'.join(str(x) for x in self.sorted_players())
    s += "\n\nProjected Score: %s" % self.projected()
    s += "\tCost: $%s" % self.spent()
    return s

SALARY_CAP = 50000

POSITION_LIMITS = [
  ["QB", 2, 2],
  ["RB", 2, 4],
  ["WR", 3, 5]
]

NUMBER_OF_LINEUPS = 3

ROSTER_SIZE = 9
UNIQUE_PLAYERS = 7

def get_index(players, target):
  for i, player in enumerate(players):
    if player.name == target.name:
      return i

def optimize(player_pool, existing_rosters):
  solver = pywraplp.Solver('DK', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  objective = solver.Objective()
  objective.SetMaximization()

  variables = []

  for player in player_pool:
    if player.lock:
      variables.append(solver.IntVar(1, 1, player.name))
    elif player.ban:
      variables.append(solver.IntVar(0, 0, player.name))
    else:      
      variables.append(solver.IntVar(0, 1, player.name))

  for i, player in enumerate(player_pool):
    objective.SetCoefficient(variables[i], player.projected)

  salary_cap = solver.Constraint(0, SALARY_CAP)
  for i, player in enumerate(player_pool):
    salary_cap.SetCoefficient(variables[i], player.salary)

  for position, min_limit, max_limit in POSITION_LIMITS:
    position_cap = solver.Constraint(min_limit, max_limit)

    for i, player in enumerate(player_pool):
      if position == player.position:
        position_cap.SetCoefficient(variables[i], 1)

  size_cap = solver.Constraint(ROSTER_SIZE, ROSTER_SIZE)
  for variable in variables:
    size_cap.SetCoefficient(variable, 1)

  for roster in existing_rosters:
    unique_players = solver.Constraint(0, UNIQUE_PLAYERS)
    for player in roster.sorted_players():
      i = get_index(player_pool, player)
      unique_players.SetCoefficient(variables[i], 1)

  solution = solver.Solve()

  if solution == solver.OPTIMAL:
    roster = Roster()

    for i, player in enumerate(player_pool):
      if variables[i].solution_value() == 1:
        roster.add_player(player)

    return roster
  else:
    print "No solution :("


if __name__ == "__main__":
  player_pool = []
  with open('projections/cfb_week11_late.csv', 'rb') as csv_file:
    csv_data = csv.DictReader(csv_file, skipinitialspace=True)

    for row in csv_data:
      player_pool.append(Player(row))

  print "Optimal CFB rosters for: $%s\n" % SALARY_CAP
  
  rosters = []
  for i in range(0, NUMBER_OF_LINEUPS):
    roster = optimize(player_pool, rosters)
    
    if roster is None:
      print "Couldn't generate enough rosters :("
      break
    else: 
      rosters.append(roster)

    print "\t\tRoster #%s" % (i + 1)
    print roster, '\n'
