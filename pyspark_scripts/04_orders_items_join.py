
from pyspark.sql import SparkSession

# Start Spark
spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("Olist_Orders_Items_Join")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# Read orders dataset
orders = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("Data_sets/Cleaned_Dataset/cleaned_orders.csv")
)

# Read order items dataset
order_items = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("Data_sets/Cleaned_Dataset/cleaned_order_items.csv")
)

# Join both datasets using order_id
joined_df = orders.join(
    order_items,
    on="order_id",
    how="inner"
)

# Display record counts
print("Total Orders:", orders.count())
print("Total Order Items:", order_items.count())
print("Total Joined Records:", joined_df.count())

# Display sample joined records
print("\n--- ORDERS AND ORDER ITEMS ---")

joined_df.select(
    "order_id",
    "customer_id",
    "order_status",
    "product_id",
    "seller_id",
    "price"
).show(5, truncate=False)

# Stop Spark
spark.stop()
