# Constraint Solving
Find a valid work schedules
Given:
  all shifts are covered
  each employee works between 30 and 40 hours
  Bob and Jim can't work together

Find a valid lunch order
Given:
  cost of meal is less than $10
  a meal is one entre plus one or more sides
  at least 200g of protein
  no more than 10g of carbs

# Practical?
This is slightly more academic, in business we want to
somehow rank the set of valid solutions.

Find a valid work schedule => minimize cost
Find a valid lunch order => maximize total calories

# Mixed-Integer Programming
Objective:
[max|min]imize something

Constraints:
A x = b (linear)
l <= x <= u (bound)
some or all variables are integers (integrality)

"Modeling" => converting "Givens" into equations

# Fantasy Basketball
(Explain FanDuel setup)

Maximize projected pts
Given:
  9 players (2 PG, 2 SG, 2 SF, 2 PF, 1 C)
  team salary no more than $50k

# Brute-force?
26 PG
22 SG
25 SF
27 PF
20 C

(26 choose 2) * (22 choose 2) * (25 choose 2) * (27 choose 2) * (20 choose 1)
yields 158,107,950,000 possible combinations 
@10ms per to check, would take 50 years

# Enter `or-tools`
Open source project from Google that includes industry-grade combinatorial optimization solvers

C++ (with Python, Java, .NET bindings) or you can run in Google Sheets

# Code walkthrough
```python
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('FD', mode.CBC_MIXED_INTEGER_PROGRAMMING)

variables = []
variables.append(solver.IntVar(0, 1, "Lebron James"))
variables.append(solver.IntVar(0, 1, "Russell Westbrook"))
variables.append(solver.IntVar(0, 1, "Demarcus Cousins"))
...

objective = solver.Objective()
objective.SetMaximization()
objective.SetCoefficient(variables[0], 50.2)
objective.SetCoefficient(variables[1], 45.5)
objective.SetCoefficient(variables[2], 51.3)
...

salary_cap = solver.Constraint(0, 50000)
salary_cap.SetCoefficient(variables[0], 10400)
salary_cap.SetCoefficient(variables[1], 9800)
salary_cap.SetCoefficient(variables[2], 9400)
...

pg_limit = solver.Constraint(2, 2)
pg_limit.SetCoefficient(variables[0], 0)
pg_limit.SetCoefficient(variables[1], 1)
pg_limit.SetCoefficient(variables[2], 0)
...
c_limit = solver.Constraint(1, 1)
c_limit.SetCoefficient(variables[0], 0)
c_limit.SetCoefficient(variables[1], 0)
c_limit.SetCoefficient(variables[2], 1)
...

solver.Solve()


roster = []
for v in variables:
  if v.solution_value() == 1:
    roster.append(lookupPlayer(v.name)))

print roster

---
Optimal roster for: $60000

[PG] Tony Wroten         ($7600, 38.8)
[PG] Darren Collison     ($6500, 32.1)
[SG] Jimmy Butler        ($7000, 34.2)
[SG] Joe Johnson         ($6400, 32.1)
[SF] Rudy Gay            ($8400, 36.9)
[SF] Mirza Teletovic     ($4700, 21.8)
[PF] Pau Gasol           ($8600, 37.9)
[PF] Kevin Garnett       ($4700, 22.2)
[C ] Tyson Chandler      ($6000, 27.1)

Projected Score: 283.1  Cost: $59900


>> time python optimize.py
>>   0.10s user 0.02s system 97% cpu 0.124 total

``` 

# Questions

show graph



####
10 min -> 12 slides?


