from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GroupBy").getOrCreate()

# Create a sample DataFrame
sales_df = spark.createDataFrame([
    ("Bangalore", "Shirt", 20),
    ("Mysore", "Shirt", 25),
    ("Bangalore", "Jeans", 30),
    ("Chennai", "Jeans", 40),
], ["city", "item", "price"])

# Group by city
grouped_city_df = sales_df.groupBy("city")

# Group by city and item
grouped_city_item_df = sales_df.groupBy("city", "item")
