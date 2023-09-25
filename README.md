# pants-test

## Pre-Requisites

1. Python >3.9.* installed

## Demo Steps

```bash
pants list ::
pants dependencies src/module_b
pants dependents src/module_b
pants dependents src/module_a
pants dependents src/module_a --dependents-transitive
# Make a change to `src/module_b/__init__.py
pants list --changed-since=HEAD
pants list --changed-since=HEAD --changed-dependents=transitive
pants test ::
pants test --changed-since=HEAD --changed-dependents=transitive
pants package --changed-since=HEAD --changed-dependents=transitive
git checkout .
# Make a change to `src/module_d/__init__.py
pants list --changed-since=HEAD
pants package --changed-since=HEAD --changed-dependents=transitive
```