### Updates
* underscore to hyphen undone
* underscore in parameter will be replaced with ''
* observe is supported



### Tutorial
[Link to py2pddl](https://github.com/remykarem/py2pddl)

### step 1: create python file
```
python3 -m py2pddl.init aircargo.py

Then, enter the following
Name: AirCargo
Types (separated by space): cargo airport plane
Predicates (separated by space): plane_at cargo_at in_
Actions (separated by space): load unload fly
```

### step 2: modify the python file
* edit both the domain and problem class
* Methods decorated with @predicate should have empty bodies.
* Methods decorated with @action return a tuple of two lists.

### generate pddl files
```
python3 -m py2pddl.parse aircargo.py
```

### run downward
```
./downward/fast-downward.py problem2.pddl --search "astar(lmcut())"
```

### view plan
```
cat sas_plan
```

### medicine
```
python3 -m py2pddl.parse medicine.py
```
### run contingency planner
```
./FF -o domain.pddl -f problem.pddl -a 0
```

