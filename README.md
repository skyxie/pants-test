# pants-test

## Pre-Requisites

1. Python >3.8.* installed
2. Install and use OpenJDK8

    brew install adoptopenjdk8
    jdk 1.8

## Running without pants

    pip install -r 3rdparty/requirements.txt
    pip install pytest
    PYTHONPATH=src pytest test/test_my_module.py 

**Expected**: :white_check_mark:

**Actual**: :white_check_mark:

## Running with pants

    ./pants fmt lint check test ::

**Expected**: :white_check_mark:

**Actual**: :x:
