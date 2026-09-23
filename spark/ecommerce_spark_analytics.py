from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    sum,
    count,
    col,
    desc,
    date_format
)

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("Ecommerce Analytics") \
    .master("local[*]") \
    .getOrCreate()

# 2. Read processed Parquet data
df = spark.read.parquet(
    "data/processed/ecommerce_sales.parquet"
)

print("\n========== PROCESSED DATA ==========")
df.show()

# 3. Total Revenue
print("\n========== TOTAL REVENUE ==========")

total_revenue = df.filter(
    col("status") == "Completed"
).agg(
    sum("revenue").alias("total_revenue")
)

total_revenue.show()

# 4. Revenue by City
print("\n========== REVENUE BY CITY ==========")

revenue_by_city = df.filter(
    col("status") == "Completed"
).groupBy(
    "city"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    desc("total_revenue")
)

revenue_by_city.show()

# 5. Revenue by Product
print("\n========== REVENUE BY PRODUCT ==========")

revenue_by_product = df.filter(
    col("status") == "Completed"
).groupBy(
    "product_id",
    "name"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    desc("total_revenue")
)

revenue_by_product.show()

# 6. Order Status Summary
print("\n========== ORDER STATUS SUMMARY ==========")

status_summary = df.groupBy(
    "status"
).agg(
    count("order_id").alias("total_orders")
).orderBy(
    desc("total_orders")
)

status_summary.show()

# 7. Customer-wise Spending
print("\n========== CUSTOMER-WISE SPENDING ==========")

customer_spending = df.filter(
    col("status") == "Completed"
).groupBy(
    "customer_id",
    "name"
).agg(
    sum("revenue").alias("total_spent")
).orderBy(
    desc("total_spent")
)

customer_spending.show()

# 8. Monthly Revenue
print("\n========== MONTHLY REVENUE ==========")

monthly_revenue = df.filter(
    col("status") == "Completed"
).withColumn(
    "month",
    date_format("order_date", "yyyy-MM")
).groupBy(
    "month"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    "month"
)

monthly_revenue.show()

# 9. Stop Spark
spark.stop()

print("\n========== ANALYTICS COMPLETED ==========")