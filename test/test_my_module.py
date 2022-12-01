from pyspark.sql.types import IntegerType, StructField, StructType

from my_module import times_two


def test_my_module_udf(spark):
    df = spark.createDataFrame(
        [(1,), (2,), (3,)], schema=StructType([StructField("a", IntegerType(), False)])
    )
    result = [(row.a, row.b) for row in df.withColumn("b", times_two("a")).collect()]
    assert result == [(1, 2), (2, 4), (3, 6)]
