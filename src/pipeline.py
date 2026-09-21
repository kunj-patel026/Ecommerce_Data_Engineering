from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    print("========== DATA PIPELINE STARTED ==========")

    # Step 1: Extract
    data = extract_data()

    # Step 2: Transform
    transformed_data = transform_data(data)

    # Step 3: Load
    load_data(transformed_data)

    print("========== DATA PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    main()