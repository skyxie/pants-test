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

python_sources(
    name="module_c",
    sources=["module_c/*.py"],
    dependencies=[":module_b"],
)

python_sources(
    name="module_d",
    sources=["module_d/*.py"],
    dependencies=[":module_a"],
)