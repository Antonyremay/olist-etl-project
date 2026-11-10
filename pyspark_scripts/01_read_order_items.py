
from pyspark.sql import SparkSession

spark = (SparkSession.builder.master("local[*]").appName("Olist_Order_Items").getOrCreate())

# Reduce unnecessary Spark log messages
spark.sparkContext.setLogLevel("ERROR")

# Read the cleaned Olist CSV
file_path = "Data_sets/Cleaned_Dataset/cleaned_order_items.csv"

order_items_df = (spark.read.option("header", True).option("inferSchema", True).csv(file_path))

# Display dataset structure
print("\n--- DATASET SCHEMA ---")
order_items_df.printSchema()

# Count records
print("\n--- TOTAL RECORDS ---")
print(order_items_df.count())

# Display first five rows
print("\n--- FIRST FIVE ROWS ---")
order_items_df.show(5)

# Stop Spark
spark.stop()
