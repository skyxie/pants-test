import os
import sys
from unittest.mock import patch

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session", name="spark")
def _spark():
    with patch.dict(
        os.environ,
        {"PYSPARK_PYTHON": sys.executable, "PYSPARK_DRIVER_PYTHON": sys.executable},
    ):
        session = (
            SparkSession.builder.master("local").appName("test_my_module").getOrCreate()
        )
        session.sparkContext.setLogLevel("WARN")

        yield session

        session.stop()
