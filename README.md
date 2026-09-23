![Python](https://img.shields.io/badge/Python-3.x-blue)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-PySpark-orange)
![SQL](https://img.shields.io/badge/SQL-MySQL-blue)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-ETL-green)
![Storage](https://img.shields.io/badge/Storage-Parquet-purple)

# E-Commerce Data Engineering Pipeline

An end-to-end **Data Engineering project** that demonstrates how raw e-commerce data can be extracted, transformed, validated, stored, and analyzed using **Python, Pandas, SQL, Apache Spark, and PySpark**.

The project simulates a real-world e-commerce data pipeline using multiple raw CSV datasets. The data is processed through both a **Pandas-based ETL pipeline** and a **PySpark-based ETL pipeline**, followed by data quality validation and business analytics.

---

## Project Architecture

```text
                         RAW DATA
                            │
                            ▼
                  ┌───────────────────┐
                  │   CSV Datasets    │
                  │                   │
                  │ Customers         │
                  │ Products          │
                  │ Orders            │
                  │ Order Items       │
                  └─────────┬─────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
       ┌─────────────────┐     ┌─────────────────┐
       │   Pandas ETL    │     │   PySpark ETL   │
       │                 │     │                 │
       │ Extract         │     │ Read CSV        │
       │ Transform       │     │ Join datasets   │
       │ Load            │     │ Calculate       │
       │                 │     │ Revenue         │
       └────────┬────────┘     └────────┬────────┘
                │                       │
                ▼                       ▼
       ┌─────────────────┐     ┌─────────────────┐
       │ Pandas Parquet  │     │ Spark Parquet   │
       │     Output      │     │     Output      │
       └────────┬────────┘     └────────┬────────┘
                │                       │
                └───────────┬───────────┘
                            ▼
                  ┌───────────────────┐
                  │ Data Quality      │
                  │ Checks            │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Business          │
                  │ Analytics         │
                  └───────────────────┘
```

---

## Technologies

* Python
* Pandas
* SQL
* MySQL
* Apache Spark
* PySpark
* CSV
* Parquet
* ETL
* Data Quality Checks
* Git & GitHub

---

## Project Structure

```text
Ecommerce_Data_Engineering/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── order_items.csv
│   │
│   └── processed/
│       ├── .gitkeep
│       ├── ecommerce_sales.parquet
│       └── pandas_ecommerce_sales.parquet
│
├── src/
│   ├── .gitkeep
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── spark/
│   ├── ecommerce_spark_etl.py
│   ├── ecommerce_spark_analytics.py
│   └── data_quality_check.py
│
├── sql/
│   └── analytics_queries.sql
│
├── analytics_output.txt
├── .gitignore
└── README.md
```

---

## Raw Datasets

The project uses four raw CSV datasets.

### Customers

Contains customer information such as:

* Customer ID
* Customer Name
* City
* Signup Date

### Products

Contains product information such as:

* Product ID
* Product Name
* Category
* Price

### Orders

Contains order information such as:

* Order ID
* Customer ID
* Order Date
* Order Status

### Order Items

Contains information about products included in each order:

* Order Item ID
* Order ID
* Product ID
* Quantity

---

## ETL Implementations

The project contains two ETL implementations.

### 1. Pandas ETL Pipeline

The Pandas pipeline is implemented inside the `src/` directory.

```text
src/
├── extract.py
├── transform.py
├── load.py
└── pipeline.py
```

#### Extract

`extract.py` reads the four raw CSV datasets using Pandas.

#### Transform

`transform.py` performs:

* Date conversion
* Duplicate removal
* Dataset joins
* Product price enrichment
* Revenue calculation
* Customer and order information enrichment

Revenue is calculated as:

```text
Revenue = Quantity × Price
```

#### Load

`load.py` writes the transformed dataset to:

```text
data/processed/pandas_ecommerce_sales.parquet
```

#### Pipeline

`pipeline.py` orchestrates the complete workflow:

```text
Extract → Transform → Load
```

Run the Pandas pipeline using:

```bash
python src/pipeline.py
```

---

### 2. PySpark ETL Pipeline

The PySpark pipeline is implemented inside the `spark/` directory.

```text
spark/
├── ecommerce_spark_etl.py
├── ecommerce_spark_analytics.py
└── data_quality_check.py
```

The PySpark ETL pipeline:

1. Reads raw CSV datasets
2. Joins customers, products, orders, and order items
3. Calculates revenue
4. Creates the processed Parquet dataset

The Spark output is stored in:

```text
data/processed/ecommerce_sales.parquet
```

Run the PySpark ETL pipeline using:

```bash
python spark/ecommerce_spark_etl.py
```

The PySpark pipeline successfully processed **18 records**.

---

## Data Transformation Logic

The datasets are connected using the following relationships:

```text
Orders
   │
   ├── Customer ID → Customers
   │
   └── Order ID → Order Items
                         │
                         └── Product ID → Products
```

Revenue calculation:

```text
Revenue = Quantity × Price
```

---

## Data Quality Checks

The project includes automated data quality validation using PySpark.

The following checks are performed:

* Total record count
* NULL value validation
* Negative quantity detection
* Negative price detection
* Invalid order status detection
* Duplicate `order_item_id` detection

Current dataset validation result:

```text
Total Records: 18

Negative Quantity Records: 0
Negative Price Records: 0
Invalid Status Records: 0
Duplicate order_item_id: 0

DATA QUALITY CHECK PASSED
```

Run the data quality checks using:

```bash
python spark/data_quality_check.py
```

---

## Spark Analytics

The project uses PySpark to generate business analytics from the processed Parquet dataset.

### Analytics Performed

* Total completed revenue
* Revenue by city
* Revenue by product
* Order status summary
* Customer-wise spending
* Monthly revenue

Completed-order revenue generated by the current dataset:

```text
₹171,700
```

Run Spark analytics using:

```bash
python spark/ecommerce_spark_analytics.py
```

---

## SQL Analytics

The project also contains MySQL analytics queries covering:

* Total customers
* Total products
* Total orders
* Orders by status
* Products above a specified price
* Quantity sold by product
* Revenue by product
* Revenue by city
* Customer-wise spending
* Monthly revenue

SQL file:

```text
sql/analytics_queries.sql
```

---

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/kunj-patel026/Ecommerce_Data_Engineering.git
```

### Step 2: Open the Project

```bash
cd Ecommerce_Data_Engineering
```

### Step 3: Run Pandas ETL

```bash
python src/pipeline.py
```

This creates:

```text
data/processed/pandas_ecommerce_sales.parquet
```

### Step 4: Run PySpark ETL

```bash
python spark/ecommerce_spark_etl.py
```

This creates the Spark processed dataset:

```text
data/processed/ecommerce_sales.parquet
```

### Step 5: Run Data Quality Checks

```bash
python spark/data_quality_check.py
```

### Step 6: Run Spark Analytics

```bash
python spark/ecommerce_spark_analytics.py
```

---

## Key Data Engineering Concepts Demonstrated

This project demonstrates practical knowledge of:

* ETL pipeline development
* Data ingestion
* Data transformation
* Dataset joins
* Data validation
* Data quality checks
* Revenue calculations
* Pandas DataFrames
* PySpark DataFrames
* Apache Spark
* Parquet data storage
* SQL analytics
* Python scripting
* Batch data processing

---

## Project Outcome

The project demonstrates a complete mini data engineering workflow:

```text
Raw CSV Data
     ↓
Data Extraction
     ↓
Data Transformation
     ↓
Data Quality Validation
     ↓
Parquet Storage
     ↓
Business Analytics
```

The project also demonstrates the implementation of the ETL workflow using both **Pandas** and **PySpark**, providing practical exposure to traditional Python-based processing as well as distributed data processing concepts.

---

## Author

**Kunj Patel**

MCA Graduate | Learning Data Engineering

GitHub: https://github.com/kunj-patel026

LinkedIn: https://www.linkedin.com/in/kunj-patel-7617b91b5/
