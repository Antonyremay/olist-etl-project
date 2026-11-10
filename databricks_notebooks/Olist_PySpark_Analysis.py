# Databricks notebook source
print("Hello, Databricks!")
print("Starting Olist PySpark analysis")

# COMMAND ----------

# Read the Olist order items CSV file
order_items_df = spark.read .option("header", True) .option("inferSchema", True) .csv("/Volumes/workspace/default/olist_data/cleaned_order_items.csv")

# Display the first 5 records
display(order_items_df.limit(5))

# COMMAND ----------

# Display column names and data types
order_items_df.printSchema()

# Count total records
print("Total records:", order_items_df.count())

# COMMAND ----------

from pyspark.sql.functions import col

# Filter products with a price greater than 100
expensive_items_df = order_items_df.filter(col("price") > 100)

# Display the first 10 filtered records
display(expensive_items_df.limit(10))

print("Original records:", order_items_df.count())

print("Filtered records:", expensive_items_df.count())

# COMMAND ----------

from pyspark.sql.functions import col, count, sum, avg

# Group records by seller and calculate business metrics
seller_sales_df = order_items_df.groupBy("seller_id").agg(
    count("*").alias("total_items"),
    sum("price").alias("total_sales"),
    avg("price").alias("average_price"))

# Sort sellers by highest sales
seller_sales_df = seller_sales_df.orderBy(
    col("total_sales").desc())

# Display the top 10 sellers
display(seller_sales_df.limit(10))

# COMMAND ----------



# COMMAND ----------

# Read the cleaned orders CSV
orders_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("/Volumes/workspace/default/olist_data/cleaned_orders.csv")

# Display the first 5 records
display(orders_df.limit(5))

# COMMAND ----------

# Join orders and order items using order_id
joined_df = orders_df.join(
    order_items_df,
    on="order_id",
    how="inner"
)

# Display the first 10 records
display(joined_df.limit(10))

# COMMAND ----------

print("Orders records:", orders_df.count())

print("Order Items records:", order_items_df.count())

print("Joined records:", joined_df.count())
seller_sales_df.write.saveAsTable("workspace.default.olist_seller_sales")

# COMMAND ----------

joined_df.write.saveAsTable("workspace.default.olist_orders_items")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.default;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     seller_id,
# MAGIC     total_items,
# MAGIC     ROUND(total_sales, 2) AS total_sales,
# MAGIC     ROUND(average_price, 2) AS average_price
# MAGIC FROM workspace.default.olist_seller_sales
# MAGIC ORDER BY total_sales DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(DISTINCT order_id) AS unique_orders,
# MAGIC     ROUND(SUM(price), 2) AS total_sales
# MAGIC FROM workspace.default.olist_orders_items;