Playing around with using Google's [or-tools][ot] to optimize daily fantasy rosters.

Currently, the Python bindings for or-tools are not easy to install, so that is left as an exercise for the reader :)

---

Progress:

Given a csv with player projections (`projections.csv`), running:

`python optimize.py`

will output an optimal NBA lineup using FanDuel scoring/roster restrictions.

[ot]: https://developers.google.com/optimization/