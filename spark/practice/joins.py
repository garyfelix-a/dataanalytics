from pyspark.sql import SparkSession

spark = SparkSession.Builder.appName("joins").getOrCreate()

data1 = [("1", "felix"), ("2", "randy")]
df1 = spark.createDataFrame(data1, ["id", "name"])

data2 = [("1", "salem"), ("2", "chennai")]
df2 = spark.createDataFrame(data2, ["id", "city"])

df1.show()
df2.show()

df1.join(df2, df1.id == df2.id, "inner").show()

df1.createOrReplaceTempView("student")
df2.createOrReplaceTempView("address")

query = """
    select id, name, city from student
    left join address
    on student.id == address.id;
"""

spark.sql(query).show()