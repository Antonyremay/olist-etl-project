from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Start Spark

spark=SparkSession.builder.master("local[*]").appName("Olist_Seller_Sales").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Read Order Items

df=spark.read.option("header",True).option("inferSchema",True).csv("Data_sets/Cleaned_Dataset/cleaned_order_items.csv")

#  Group data by seller
seller_sales = (
    df.groupBy("seller_id")
    .agg(F.count("*").alias("total_items_sold"),F.round(F.sum("price"), 2).alias("total_sales"),
        F.round(F.avg("price"), 2).alias("average_price"),
        F.round(F.sum("freight_value"), 2).alias("total_freight")
    )
)

#  Display top 10 sellers
top_sellers = seller_sales.orderBy(
    F.desc("total_sales")
)

print("\n--- TOP 10 SELLERS BY TOTAL SALES ---")
top_sellers.show(10, truncate=False)

# Display overall sales
print("\n--- OVERALL SALES ---")
df.select(
    F.round(F.sum("price"), 2).alias("overall_product_sales"),
    F.round(F.sum("freight_value"), 2).alias("overall_freight")
).show()

# Stop Spark
spark.stop()