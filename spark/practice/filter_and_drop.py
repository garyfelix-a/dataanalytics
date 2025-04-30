from pyspark.sql import SparkSession

spark = SparkSession.Builder.appName().getOrCreate()

data = [("Randy", "23"),
        ("Ortan", "33"),
        ("John", "43")
        ]

df = spark.createDataFrame(data, ["name", "age"])

filter_df = df.filter()