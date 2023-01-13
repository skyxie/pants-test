python_sources(
    name="module_a",
    sources=["module_a/*.py"],
    dependencies=["3rdparty:reqs"],
    resolve="my_module"
)

python_sources(
    name="module_b",
    sources=["module_b/*.py"],
    dependencies=[":module_a"],
    resolve="my_module"
)