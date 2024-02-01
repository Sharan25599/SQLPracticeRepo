from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataFrameSort").getOrCreate()

# Create a sample DataFrame
df = spark.createDataFrame([(1, "Alice", 23), (2, "Bob", 25), (3, "Charlie", 20)], ["id", "name", "age"])

# Sort by age in ascending order using orderBy()
sorted_df = df.orderBy("age")

# Sort by age in ascending order using sort()
sorted_df = df.sort("age")

# Print the sorted DataFrame
sorted_df.show()

# Sort by age in ascending order and then by name in descending order
sorted_df = df.orderBy("age", "name", ascending=[True, False])

# Alternatively, use sort()
sorted_df = df.sort("age", "name", ascending=(True, False))

sorted_df.show()
