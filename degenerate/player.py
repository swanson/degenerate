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

  def __json___(self):
    return {
        "name": self.name,
        "position": self.position,
        "salary": self.salary,
        "projection": self.projected,
        "locked": self.lock,
        "banned": self.ban
    }