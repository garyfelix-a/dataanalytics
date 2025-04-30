from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, avg
from pyspark.sql.types import StringType

spark = SparkSession.Builder.appName("udf").getOrCreate()

data = [("john",), ("mike",), ("sara",)]
# rdd = spark.parallalize(data)

df = spark.createDataFrame(data, ["name"])

df.show()

def upper_case(name):
    return name.upper()

upper_case_udf = udf(upper_case, StringType())

df.withColumn("upper_name", upper_case_udf("name")).show()


df1

df2

df1.join(df2, df1.id == df2.id, "inner").show()

df.select("name").show()

df.select(avg("salary")).show()

df.select