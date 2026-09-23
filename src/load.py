import os


def load_data(transformed_data):
    # Create processed folder if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)

    # Output file
    output_file = "data/processed/pandas_ecommerce_sales.parquet"

    # Save transformed data
    transformed_data.to_parquet(
        output_file,
        index=False
    )

    print("Data loaded successfully!")
    print(f"File created: {output_file}")


if __name__ == "__main__":
    print("Run pipeline.py to execute the complete ETL pipeline.")