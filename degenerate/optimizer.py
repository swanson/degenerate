from ortools.linear_solver import pywraplp
from roster import Roster

class Optimizer:
  def generate_roster(self, player_pool, roster_definition, existing_rosters, unique_players): 
    self.player_pool = player_pool
    self.roster_definition = roster_definition
    self.existing_rosters = existing_rosters
    self.unique_players = unique_players

    self._build_solver()
    self._build_variables()
    self._build_objective()

    self._build_constraints()

    return self._solve()

  def _build_solver(self):
    self.solver = pywraplp.Solver('Solver', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  def _build_variables(self):
    self.variables = []  

    for player in self.player_pool:
      if player.lock:
        self.variables.append(self._locked_player(player))
      elif player.ban:
        self.variables.append(self._banned_player(player))
      else:      
        self.variables.append(self._eligible_player(player))

  def _locked_player(self, player):
    return self.solver.IntVar(1, 1, player.name)

  def _banned_player(self, player):
    return self.solver.IntVar(0, 0, player.name)

  def _eligible_player(self, player):
    return self.solver.IntVar(0, 1, player.name)

  def _build_objective(self):
    self.objective = self.solver.Objective()
    self.objective.SetMaximization()

    for i, player in enumerate(self.player_pool):
      self.objective.SetCoefficient(self.variables[i], player.projected)

  def _build_constraints(self):
    self._constrain_roster_size()
    self._constrain_positions()
    self._constrain_salary()
    self._constrain_unique_players()

  def _constrain_roster_size(self):
    max_size = self._max_roster_size()
    size_cap = self.solver.Constraint(max_size, max_size)
  
    for variable in self.variables:
      size_cap.SetCoefficient(variable, 1)

  def _constrain_salary(self):
    salary_cap = self.solver.Constraint(0, self._max_salary())

    for i, player in enumerate(self.player_pool):
      salary_cap.SetCoefficient(self.variables[i], player.salary)

  def _constrain_positions(self):
    for position, min_limit, max_limit in self._position_limits():
      position_cap = self.solver.Constraint(min_limit, max_limit)

      for i, player in enumerate(self.player_pool):
        if position == player.position:
          position_cap.SetCoefficient(self.variables[i], 1)

  def _constrain_unique_players(self):
    for roster in self.existing_rosters:
      unique_players = self.solver.Constraint(0, self.unique_players)

      for player in roster.sorted_players():
        i = self._get_index_by_name(self.player_pool, player.name)
        unique_players.SetCoefficient(self.variables[i], 1)

  def _get_index_by_name(self, players, target):
    for i, player in enumerate(players):
      if player.name == target:
        return i

  def _solve(self):
    solution = self.solver.Solve()

    if solution == self.solver.OPTIMAL:
      
      return self._build_roster()
    else:
      return None

  def _build_roster(self):
    roster = Roster()

    for i, player in enumerate(self.player_pool):
      if self._player_is_included(i):
        roster.add_player(player)

    return roster

  def _player_is_included(self, index):
    return self.variables[index].solution_value() == 1

  def _max_roster_size(self):
    return self.roster_definition['roster_size']

  def _max_salary(self):
    return self.roster_definition['salary_cap']

  def _position_limits(self):
    return self.roster_definition['position_limits']



