
import pandas as pd
from sqlalchemy import create_engine, URL, text
from dotenv import load_dotenv
from pathlib import Path
import os

# Loading Environment Variables

project_path = Path(__file__).resolve().parent.parent
load_dotenv(project_path / ".env")


# MySQL Database Connection

connection_url = URL.create(
    "mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 3306)),
    database=os.getenv("DB_NAME")
)

engine = create_engine(connection_url)


# Testing Database Connection

def test_connection():

    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE()"))
        print("Connected to MySQL Successfully!")
        print("Database:", result.scalar())

# Loading Cleaned Datasets

def load_cleaned_data():

    cleaned_path = project_path / "Data_sets" / "Cleaned_Dataset"
    data_path = project_path / "Data_sets"

    
    datasets = {
    "geolocation": cleaned_path / "cleaned_geolocation_data.csv",
    "orders": cleaned_path / "cleaned_orders.csv",
    "order_items": cleaned_path / "cleaned_order_items.csv",
    "order_payments": cleaned_path / "cleaned_order_payments.csv",
    "customers": cleaned_path / "cleaned_customers.csv",
    "products": cleaned_path / "cleaned_products.csv",
    "reviews": cleaned_path / "cleaned_reviews.csv",
    "sellers": cleaned_path / "cleaned_sellers.csv",
    "category_translation": cleaned_path / "cleaned_category_translation.csv"}


    for table_name, file_path in datasets.items():

        print(f"\nLoading {table_name} Dataset")

        df = pd.read_csv(file_path)

        print("Source Rows:", len(df))
        print("Source Columns:", len(df.columns))

# Loading Data into MySQL

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=1000
        )

        print(f"{table_name} Loaded Successfully!")


# Validating and Reconciling Data

def validate_data():

    print("\nDATA RECONCILIATION")

    with engine.connect() as connection:

        datasets = [
            "geolocation",
            "orders",
            "order_items",
            "order_payments",
            "customers",
            "products",
            "reviews",
            "sellers",
            "category_translation"
        ]

        for table_name in datasets:

            result = connection.execute(
                text(f"SELECT COUNT(*) FROM `{table_name}`")
            )

            target_count = result.scalar()

            print(f"{table_name}: {target_count} rows in MySQL")


# Main Function

def main():

    test_connection()

    load_cleaned_data()

    validate_data()

    print("\nAll Datasets Loaded Successfully!")


if __name__ == "__main__":
    main()
