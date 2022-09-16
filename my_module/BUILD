python_sources(
    name="lib",
    sources=["my_module/**/*.py"],
    dependencies=["3rdparty:reqs"],
    resolve="my_module"
)

python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="my_module",
        version="0.1.0",
        description="lorem-ipsum",
    ),
    entry_points={
        "console_scripts": {
            "main": "my_module:main"
        }
    }
)