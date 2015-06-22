Playing around with using Google's [or-tools][ot] to optimize daily fantasy rosters.

Currently, the Python bindings for or-tools are not easy to install, so that is left as an exercise for the reader :)

Initial inspiration and data model: http://www.barelyknown.com/blog/2014/11/13/d6q2mihtpbtehi3u6sh7z8vc7rnr4f

---

Progress:

Given a csv with player projections (`projections.csv`), running:

`python optimize.py`

will output an optimal NBA lineup using FanDuel scoring/roster restrictions.

[ot]: https://developers.google.com/optimization/