from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

df = spark.table("sales_catalog.bronze.sales_bronze")

# Remove duplicate rows
df = df.dropDuplicates()

# Remove rows having null customer, product, quantity or price
df = df.dropna(subset=["customer", "product", "quantity", "price"])

# Create total_amount column
df = df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("sales_catalog.silver.sales_silver")

print("Silver table created successfully.")