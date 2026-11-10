
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Start Spark
spark = (SparkSession.builder.master("local[*]").appName("Olist_Order_Items_Quality").getOrCreate())

spark.sparkContext.setLogLevel("ERROR")

# Read the dataset
df = spark.read.option("header", True).option("inferSchema", True).csv("Data_sets/Cleaned_Dataset/cleaned_order_items.csv")

# Check total records
total_records = df.count()
print("Total records:", total_records)

# Check missing values in each column
print("\n--- NULL VALUE CHECK ---")

null_counts = df.select([F.sum(F.col(column).isNull().cast("int")).alias(column)for column in df.columns])

null_counts.show()

# Check exact duplicate rows
duplicate_count = total_records - df.dropDuplicates().count()

print("Exact duplicate rows:", duplicate_count)

# Stop Spark
spark.stop()
