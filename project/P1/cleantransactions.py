from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("FailedTransactionFilter").getOrCreate()

# Set the input and output paths in the GCS bucket
BUCKET_NAME = "felix-bucket"
CLEANED_FOLDER = f"gs://{BUCKET_NAME}/cleaned/"
FAILED_FOLDER = f"gs://{BUCKET_NAME}/failed_transactions/"

# Read the CSV file
df = spark.read.option("header", "true").option("inferSchema", "true").csv(CLEANED_FOLDER)

# Show schema to verify column names
df.printSchema()

# Filter only the failed transactions (Status is 'FAILED' or 'DECLINED')
failed_df = df.filter(col("Status").isin(["FAILED", "DECLINED"]))

# Write the failed transactions to the output folder
failed_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(FAILED_FOLDER)

print("Failed transaction filtering completed.")

# Stop the Spark session
spark.stop()
