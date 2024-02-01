import pyspark.sql as spark

# Create SparkSession
spark = spark.SparkSession.builder.appName("UnionExample").getOrCreate()

# Create DataFrames with the same schema
df1 = spark.createDataFrame([("Alice", 25), ("Bob", 30)], ["name", "age"])
df2 = spark.createDataFrame([("Charlie", 28), ("Alice", 35)], ["name", "age"])

# Use union to combine DataFrames and remove duplicates
df_combined = df1.union(df2)

# Show the resulting DataFrame
df_combined.show()

# Using unionAll will keep duplicates (deprecated):
df_combined_all = df1.unionAll(df2)
df_combined_all.show()

# To only remove duplicates manually:
df_combined_all_distinct = df_combined_all.distinct()
df_combined_all_distinct.show()
