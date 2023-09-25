python_tests(
    name="module_a-alpha",
    sources=["test_module_a.py"],
    resolve="alpha"
)

python_tests(
    name="module_a-beta",
    sources=["test_module_a.py"],
    resolve="beta"
)

python_tests(
    name="module_b-alpha",
    sources=["test_module_b.py"],
    dependencies=["3rdparty:reqs-shared#pytest"],
    resolve="alpha"
)

python_tests(
    name="module_b-beta",
    sources=["test_module_b.py"],
    dependencies=["3rdparty:reqs-shared#pytest"],
    resolve="beta"
)

python_tests(
    name="module_c",
    sources=["test_module_c.py"],
    resolve="alpha"
)

python_tests(
    name="module_d",
    sources=["test_module_d.py"],
    resolve="alpha"
)