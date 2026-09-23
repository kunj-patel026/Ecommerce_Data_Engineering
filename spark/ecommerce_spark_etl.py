from pyspark.sql import SparkSession
import logging


# ==============================
# Logging Configuration
# ==============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ==============================
# Create Spark Session
# ==============================

spark = SparkSession.builder \
    .appName("EcommerceDataEngineering") \
    .master("local[*]") \
    .getOrCreate()


logger.info("========== SPARK ETL STARTED ==========")


try:

    # ==============================
    # Read Raw CSV Data
    # ==============================

    logger.info("Reading raw CSV data...")

    customers = spark.read.option(
        "header", True
    ).option(
        "inferSchema", True
    ).csv("data/raw/customers.csv")

    products = spark.read.option(
        "header", True
    ).option(
        "inferSchema", True
    ).csv("data/raw/products.csv")

    orders = spark.read.option(
        "header", True
    ).option(
        "inferSchema", True
    ).csv("data/raw/orders.csv")

    order_items = spark.read.option(
        "header", True
    ).option(
        "inferSchema", True
    ).csv("data/raw/order_items.csv")


    logger.info("Raw CSV data loaded successfully")


    # ==============================
    # Join Data
    # ==============================

    logger.info("Joining datasets...")

    df = order_items.join(
        orders,
        "order_id"
    ).join(
        products,
        "product_id"
    ).join(
        customers,
        "customer_id"
    )


    # ==============================
    # Calculate Revenue
    # ==============================

    logger.info("Calculating revenue...")

    from pyspark.sql.functions import col

    df = df.withColumn(
        "revenue",
        col("quantity") * col("price")
    )


    # ==============================
    # Select Required Columns
    # ==============================

    df = df.select(
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "price",
        "revenue",
        "customer_id",
        "order_date",
        "status",
        "name",
        "city"
    )


    # ==============================
    # Write Parquet
    # ==============================

    logger.info("Writing processed data to Parquet...")

    df.write.mode(
        "overwrite"
    ).parquet(
        "data/processed/ecommerce_sales.parquet"
    )


    logger.info("Parquet file created successfully")

    logger.info(
        "Total processed records: %s",
        df.count()
    )


    logger.info("========== SPARK ETL COMPLETED ==========")


except Exception as e:

    logger.error(
        "ETL pipeline failed: %s",
        str(e)
    )

    raise


finally:

    spark.stop()

    logger.info("Spark session stopped")