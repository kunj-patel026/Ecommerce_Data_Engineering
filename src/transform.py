import pandas as pd


def transform_data(data):
    customers, products, orders, order_items = data

    # Convert date columns
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    # Remove duplicate records
    customers = customers.drop_duplicates()
    products = products.drop_duplicates()
    orders = orders.drop_duplicates()
    order_items = order_items.drop_duplicates()

    # Add product price
    order_items = order_items.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="left"
    )

    # Calculate revenue
    order_items["revenue"] = (
        order_items["quantity"] * order_items["price"]
    )

    # Add order information
    order_items = order_items.merge(
        orders[["order_id", "customer_id", "order_date", "status"]],
        on="order_id",
        how="left"
    )

    # Add customer information
    order_items = order_items.merge(
        customers[["customer_id", "name", "city"]],
        on="customer_id",
        how="left"
    )

    print("Data transformed successfully!")

    return order_items


if __name__ == "__main__":
    print("Run pipeline.py to execute the complete ETL pipeline.")