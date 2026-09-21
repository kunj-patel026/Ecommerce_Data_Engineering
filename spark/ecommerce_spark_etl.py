from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

# Create Spark session
spark = SparkSession.builder \
    .appName("EcommerceDataEngineering") \
    .getOrCreate()

print("========== SPARK ETL STARTED ==========")

# Read processed Parquet data
df = spark.read.parquet(
    "data/processed/ecommerce_sales.parquet"
)

print("Data loaded successfully!")

# Show data
df.show()

# Show schema
df.printSchema()

# Total revenue
total_revenue = df.select(
    sum("revenue").alias("total_revenue")
)

print("========== TOTAL REVENUE ==========")
total_revenue.show()

# Revenue by city
city_revenue = df.groupBy("city").agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    col("total_revenue").desc()
)

print("========== REVENUE BY CITY ==========")
city_revenue.show()

# Revenue by product
product_revenue = df.groupBy("product_id").agg(
    sum("revenue").alias("total_revenue"),
    sum("quantity").alias("total_quantity")
).orderBy(
    col("total_revenue").desc()
)

print("========== REVENUE BY PRODUCT ==========")
product_revenue.show()

# Count orders by status
order_status = df.groupBy("status").agg(
    count("order_id").alias("total_orders")
)

print("========== ORDERS BY STATUS ==========")
order_status.show()

print("========== SPARK ETL COMPLETED ==========")

spark.stop()