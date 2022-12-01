from pyspark.sql.functions import lit
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from my_module import get_domain, times_two


def test_times_two(spark):
    df = spark.createDataFrame(
        [(1,), (2,), (3,)], schema=StructType([StructField("a", IntegerType(), False)])
    )
    result = [(row.a, row.b) for row in df.withColumn("b", times_two("a")).collect()]
    assert result == [(1, 2), (2, 4), (3, 6)]


def test_get_domain(spark):
    df = spark.createDataFrame(
        [
            ("https://google.com",),
            ("https://whitehouse.gov",),
            ("http://tiangela.us/",),
        ],
        schema=StructType([StructField("a", StringType(), True)]),
    )
    result = [(row.a, row.b) for row in df.withColumn("b", get_domain("a")).collect()]
    assert result == [
        ("https://google.com", "google"),
        ("https://whitehouse.gov", "whitehouse"),
        ("http://tiangela.us/", "tiangela"),
    ]
