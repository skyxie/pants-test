# pants-test

## Pre-Requisites

1. Python >3.8.* installed

## Demo Steps

```bash
./pants list ::
./pants dependencies src/module_b
./pants dependees src/module_b
./pants dependees src/module_a
./pants dependees src/module_a --dependees-transitive
# Make a change to `src/module_b/__init__.py
./pants list --changed-since=HEAD
./pants list --changed-since=HEAD --changed-dependees=transitive
./pants test ::
./pants test --changed-since=HEAD --changed-dependees=transitive
./pants package --changed-since=HEAD --changed-dependees=transitive
git checkout .
# Make a change to `src/module_d/__init__.py
./pants list --changed-since=HEAD
./pants package --changed-since=HEAD --changed-dependees=transitive
```