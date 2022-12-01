python_source(
    name="conftest",
    source="conftest.py",
    dependencies=["3rdparty:reqs"],
)

python_tests(
    name="my_module",
    sources=["test_my_module.py"],
    dependencies=["src:my_module", ":conftest"],
)