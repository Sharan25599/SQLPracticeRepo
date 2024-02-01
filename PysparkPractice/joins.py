from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("JoinExample").getOrCreate()

# Create DataFrames
customers = spark.createDataFrame([
    (1, "Hemanth", "Bangalore"),
    (2, "Rahul", "Chennai"),
], ["customer_id", "name", "city"])

orders = spark.createDataFrame([
    (101, 1, "Book", 10.0),
    (102, 2, "Shirt", 25.0),
    (103, 1, "Pen", 5.0),
], ["order_id", "customer_id", "product", "price"])

# Inner join on customer_id
joined_df = customers.join(orders, on="customer_id",how="inner")

# Show the joined DataFrame
joined_df.show()

# Left outer join
joined_df = customers.join(orders, on="customer_id", how="left")
joined_df.show()

# Right outer join
joined_df = customers.join(orders, on="customer_id", how="right")
joined_df.show()

# Full outer join
joined_df = customers.join(orders, on="customer_id", how="full")
joined_df.show()

# Left semi join
joined_df = customers.join(orders, on="customer_id", how="leftsemi")
joined_df.show()

# Left Anti join
joined_df = customers.join(orders, on="customer_id", how="leftanti")
joined_df.show()

# Cross Join
joined_df = customers.crossJoin(orders)
joined_df.show()




