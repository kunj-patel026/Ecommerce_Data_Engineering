import pandas as pd


def extract_data():
    customers = pd.read_csv("data/raw/customers.csv")
    products = pd.read_csv("data/raw/products.csv")
    orders = pd.read_csv("data/raw/orders.csv")
    order_items = pd.read_csv("data/raw/order_items.csv")

    print("Data extracted successfully!")

    return customers, products, orders, order_items


if __name__ == "__main__":
    extract_data()