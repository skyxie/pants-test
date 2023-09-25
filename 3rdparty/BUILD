python_requirements(
    name="reqs-alpha",
    description="3rd party dependencies for resolve alpha",
    source="requirements-alpha.txt",
    resolve="alpha"
)

python_requirements(
    name="reqs-beta",
    description="3rd party dependencies for resolve beta",
    source="requirements-beta.txt",
    resolve="beta"
)

python_requirements(
    name="reqs-shared",
    description="3rd party dependencies shared between resolves alpha and beta",
    source="requirements-shared.txt",
    resolve=parametrize("alpha", "beta")
)

python_requirements(
    name="reqs-dev",
    description="Requirements for dev utilities such as black, mypy, pylint",
    source="requirements-dev.txt",
    resolve="dev"
)