Daily fantasy optimizer, built on Google's [or-tools][ot]

Currently, the Python bindings for or-tools are not easy to install, so that is left as an exercise for the reader :)

Initial inspiration and data model: http://www.barelyknown.com/blog/2014/11/13/d6q2mihtpbtehi3u6sh7z8vc7rnr4f

---

Linear constraint-based daily fantasy lineup optimizer, with support for position limits, flex spots, and lock/ban. Generates top N lineups, with support for number of unique players per lineup. Fast (sub-second computations).

`optimize_cfb.py` has the most features :)

Example
```
>> python optimize_cfb.py
Optimal CFB rosters for: $50000
Unique players per roster: 8

        Roster #1
[QB] Greg Ward Jr.       ($8500, 34.2) LOCK
[QB] Gunner Kiel         ($8000, 36.2) 
[RB] Keith Harrington    ($3200, 11.2) 
[RB] Marteze Waller      ($5000, 17.6) 
[RB] Mike Boone          ($4200, 15.6) 
[RB] Paul Harris         ($4500, 24.8) 
[WR] Rashard Higgins     ($6400, 23.1) 
[WR] Shaq Washington     ($6100, 19.9) LOCK
[WR] Phil Mayhue         ($3800, 12.0) 

Projected Score: 194.6  Cost: $49700 

        Roster #2
[QB] Greg Ward Jr.       ($8500, 34.2) LOCK
[QB] Gunner Kiel         ($8000, 36.2) 
[RB] Dalyn Dawkins       ($4300, 14.0) 
[RB] Daniel Lasco        ($4100, 14.6) 
[RB] Mike Boone          ($4200, 15.6) 
[RB] Paul Harris         ($4500, 24.8) 
[WR] Rashard Higgins     ($6400, 23.1) 
[WR] Shaq Washington     ($6100, 19.9) LOCK
[WR] Phil Mayhue         ($3800, 12.0) 

Projected Score: 194.4  Cost: $49900 

        Roster #3
[QB] Greg Ward Jr.       ($8500, 34.2) LOCK
[QB] Gunner Kiel         ($8000, 36.2) 
[RB] Keith Harrington    ($3200, 11.2) 
[RB] Marteze Waller      ($5000, 17.6) 
[RB] Mike Boone          ($4200, 15.6) 
[RB] Paul Harris         ($4500, 24.8) 
[WR] Austin Hooper       ($4000, 11.4) 
[WR] Rashard Higgins     ($6400, 23.1) 
[WR] Shaq Washington     ($6100, 19.9) LOCK

Projected Score: 194.0  Cost: $49900 
```

[ot]: https://developers.google.com/optimization/