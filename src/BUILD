python_sources(
    name="module_a-alpha",
    sources=["module_a/*.py"],
    dependencies=[
        "3rdparty:reqs-alpha#pandas",
        "3rdparty:reqs-alpha#numpy"
    ],
    resolve="alpha"
)

python_sources(
    name="module_a-beta",
    sources=["module_a/*.py"],
    dependencies=[
        "3rdparty:reqs-beta#pandas",
        "3rdparty:reqs-beta#numpy",
    ],
    resolve="beta"
)

python_sources(
    name="module_b",
    sources=["module_b/*.py"],
    dependencies=["3rdparty:reqs-shared#pretty-tables"],
    resolve=parametrize("alpha", "beta")
)

python_sources(
    name="module_c",
    sources=["module_c/*.py"],
    resolve="alpha"
)

python_sources(
    name="module_d",
    sources=["module_d/*.py"],
    resolve="alpha"
)

python_distribution(
    name="dist_c",
    dependencies=[":module_c"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="pants-test-c",
        version="0.1.0",
        description="Just a stoopid test",
    ),
)
