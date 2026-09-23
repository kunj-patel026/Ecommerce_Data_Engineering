from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("Ecommerce Data Quality Check") \
    .master("local[*]") \
    .getOrCreate()

# 2. Read processed data
df = spark.read.parquet(
    "data/processed/ecommerce_sales.parquet"
)

print("\n========== DATA QUALITY CHECK ==========")

# 3. Check total records
total_records = df.count()

print("\nTotal Records:", total_records)

# 4. Check NULL values
print("\n========== NULL VALUE CHECK ==========")

null_check = df.select([
    count(
        col(c)
    ).alias(c)
    for c in df.columns
])

null_check.show()

# 5. Check negative quantity
print("\n========== NEGATIVE QUANTITY CHECK ==========")

negative_quantity = df.filter(
    col("quantity") < 0
).count()

print("Negative Quantity Records:", negative_quantity)

# 6. Check negative price
print("\n========== NEGATIVE PRICE CHECK ==========")

negative_price = df.filter(
    col("price") < 0
).count()

print("Negative Price Records:", negative_price)

# 7. Check invalid status
print("\n========== STATUS CHECK ==========")

valid_status = ["Completed", "Cancelled", "Pending"]

invalid_status = df.filter(
    ~col("status").isin(valid_status)
).count()

print("Invalid Status Records:", invalid_status)

# 8. Check duplicate order_item_id
print("\n========== DUPLICATE CHECK ==========")

duplicate_records = df.groupBy(
    "order_item_id"
).count().filter(
    col("count") > 1
).count()

print("Duplicate order_item_id:", duplicate_records)

# 9. Final result
print("\n========== FINAL DATA QUALITY RESULT ==========")

if (
    negative_quantity == 0
    and negative_price == 0
    and invalid_status == 0
    and duplicate_records == 0
):
    print("DATA QUALITY CHECK PASSED")
else:
    print("DATA QUALITY CHECK FAILED")

# 10. Stop Spark
spark.stop()