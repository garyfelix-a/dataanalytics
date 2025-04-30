from pyspark.sql import SparkSession
import spark

spark = SparkSession.Builder.appName("SelectingExample").getOrCreate()

data = [("John", 23, "USA"), ("Sara", 25, "UK")]
columns = ["name", "age", "country"]

df = spark.createDataFrame(data, columns)

df.select("name", "columns").show()