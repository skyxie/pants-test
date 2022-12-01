import tldextract
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, StringType

__version__ = "0.1.0"
__author__ = "Tian Xie <tian.xie@enigma.com>"


@udf(returnType=IntegerType())
def times_two(base):
    return base * 2


@udf(returnType=StringType())
def get_domain(url):
    return tldextract.extract(url).domain
