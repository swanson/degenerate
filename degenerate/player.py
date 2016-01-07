class Player:
  def __init__(self, opts):
    self.name = opts['player']
    self.position = opts['position'].upper()
    self.salary = int(opts['salary'])
    self.projected = float(opts['projection'])
    self.lock = int(opts['lock']) > 0
    self.ban = int(opts['lock']) < 0

  @classmethod
  def from_json(cls, json):
    lock = 0
    if json['locked']:
        lock = 1
    if json['banned']:
        lock = -1

    data = {
        'player': json['name'],
        'position': json['position'],
        'salary': json['salary'],
        'projection': json['projection'],
        'lock': lock
    }
    return cls(data)

  def __repr__(self):
    return "[{0: <2}] {1: <20}(${2}, {3}) {4}".format(self.position, \
                                    self.name, \
                                    self.salary,
                                    self.projected,
                                    "LOCK" if self.lock else "")

  def __json__(self):
    return {
        "name": self.name,
        "position": self.position,
        "salary": self.salary,
        "projection": self.projected,
        "locked": self.lock,
        "banned": self.ban
    }