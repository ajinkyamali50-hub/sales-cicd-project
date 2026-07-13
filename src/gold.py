from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.getOrCreate()

# Read Silver table
df = spark.table("sales_catalog.silver.sales_silver")

# Aggregate data
gold_df = (
    df.groupBy("product")
      .agg(
          sum("quantity").alias("total_quantity"),
          sum("total_amount").alias("total_sales")
      )
)

# Save Gold table
gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("sales_catalog.gold.sales_gold")

print("Gold table created successfully.")