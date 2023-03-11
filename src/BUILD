python_sources(
    name="module_a",
    sources=["module_a/*.py"],
    dependencies=["3rdparty:reqs"],
)

python_sources(
    name="module_b",
    sources=["module_b/*.py"],
    dependencies=[":module_a"],
)

python_requirement(name="reqs_c", requirements=["requests"])

python_sources(
    name="module_c",
    sources=["module_c/*.py"],
    dependencies=[":module_b", ":reqs_c"],
)

python_requirement(name="reqs_d", requirements=["requests"])

python_sources(
    name="module_d",
    sources=["module_d/*.py"],
    dependencies=[":module_a", ":reqs_d"],
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
