import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session", name="spark")
def _spark():
    session = (
        SparkSession.builder.master("local").appName("test_my_module").getOrCreate()
    )
    session.sparkContext.setLogLevel("WARN")

    yield session

    session.stop()
