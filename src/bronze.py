from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

input_path = "/Volumes/sales_catalog/bronze/raw_files/sales.csv"

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(input_path)
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("sales_catalog.bronze.sales_bronze")

print("Bronze table created successfully.")