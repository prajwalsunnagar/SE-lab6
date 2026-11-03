# L6_L7_58 — Restaurant Bill

Lab 6: Code and Branch Coverage

The module under test totals restaurant bills by seating section, happy hour,
and party size; splits a bill; and decides how a walk-in party is seated.

Run the line coverage suite from this folder:

```powershell
python -m coverage run --source=restaurant_bill -m pytest CodeCoverageTest_restaurant_bill.py
python -m coverage report -m
```

Run the branch coverage suite from this folder:

```powershell
python -m coverage erase
python -m coverage run --branch --source=restaurant_bill -m pytest BranchCoverageTest_restaurant_bill.py
python -m coverage report -m
```

Keep Lab 6 work in this folder. The original repository provides `test_restaurant_bill.py` as a starter; these two focused files make the handout's
separate line-coverage and branch-coverage stages explicit.

