import csv

from degenerate import Player

class PlayerPool:
  def fromCSV(self, filename):
    player_pool = []

    with open(filename, 'rb') as csv_file:
      csv_data = csv.DictReader(csv_file, skipinitialspace=True)

      for row in csv_data:
        player_pool.append(Player(row))

    return player_pool
